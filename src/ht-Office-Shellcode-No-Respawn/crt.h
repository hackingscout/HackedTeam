#ifndef __MY_CRT
#define __MY_CRT
#include <Windows.h>

BOOL __ISUPPER__(__in CHAR c);
CHAR __TOLOWER__(__in CHAR c);
UINT __STRLEN__(__in LPSTR lpStr1);
UINT __STRLENW__(__in LPWSTR lpStr1);
LPWSTR __STRSTRIW__(__in LPWSTR lpStr1, __in LPWSTR lpStr2);
INT __STRCMPI__(__in LPSTR lpStr1, __in LPSTR lpStr2);
INT __STRNCMPI__(__in LPSTR lpStr1, __in LPSTR lpStr2, __in DWORD dwLen);
INT __STRNCMPIW__(__in LPWSTR lpStr1, __in LPWSTR lpStr2, __in DWORD dwLen);

#endif __MY_CRT