@echo off
rem --------------------------------------------------
rem This script builds the source.
rem sjasmplus.exe should be located in this folder.
rem --------------------------------------------------


rem simple compile
"%~dp0\sjasmplus.exe" %1

rem compile with listings, symbols, exports
rem "%~dp0\sjasmplus.exe" --lst="%~dpn1.lst" --sym="%~dpn1.sym" --exp="%~dpn1.exp" %1

rem remove .out file
if %errorlevel% neq 0 goto end
    del "%~dpn1.out"

:end
