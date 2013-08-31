@echo off
rem ----------------------------------------------------------------------------
rem This script builds the source. At first it's search for make.bat in the
rem project folder. If it's found - call it, otherwise run ASM against asm-file.
rem Current directory at entry to this script is asm-file's directory.
rem There are two input parameters:
rem   1. filename (without path),
rem   2. project file path.
rem ----------------------------------------------------------------------------

set ASM="R:\sjasmplus.exe"

rem Run external script from project folder if exists
if exist "%2\make.bat" (
    chdir /d "%2"
    call "make.bat" %1 %2
    goto :end
)

rem Check if file exists
if not exist %1 (
    echo Source file not found!
    set errorlevel=1
    goto :end
)

rem Simple compile
"%ASM%" %1

rem Compile with listings, symbols, exports
rem "%ASM%" --lst="%~dpn1.lst" --sym="%~dpn1.sym" --exp="%~dpn1.exp" %1

rem Remove .out file
if %errorlevel% neq 0 goto :end
    del "%~dpn1.out"
    set errorlevel=0

:end
