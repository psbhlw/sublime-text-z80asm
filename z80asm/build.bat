@echo off
rem --------------------------------------------------
rem This script builds the source.
rem There is only one input parameter: filename.
rem --------------------------------------------------

set ASM="R:\sjasmplus.exe"

rem Check if file exists
if not exist %1 (
    echo File not found!
    goto :end
)

rem Simple compile
"%ASM%" %1

rem Compile with listings, symbols, exports
rem "%ASM%" --lst="%~dpn1.lst" --sym="%~dpn1.sym" --exp="%~dpn1.exp" %1

rem Remove .out file
if %errorlevel% neq 0 goto end
    del "%~dpn1.out"

:end
