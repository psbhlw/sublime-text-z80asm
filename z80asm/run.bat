@echo off
rem ----------------------------------------------------------------------------
rem This script runs the emulator. At first it's search for emul.bat in the
rem project folder. If it's found - call it, otherwise it will search for
rem .sna/.spg/.trd/.scl/.tap and call EMUL with it.
rem Current directory at entry to this script is asm-file's directory.
rem There are two input parameters:
rem   1. filename (without path),
rem   2. project file path.
rem ----------------------------------------------------------------------------

set EMUL="R:\emul\emul.exe"

rem Run external script from project folder if exists
if exist "%2\emul.bat" (
    chdir /d "%2"
    call "emul.bat" %1 %2
    goto :end
)

rem Check if .sna file exists
if exist "%~n1.sna" (
    "%EMUL%" "%~n1.sna"
    goto :end
)

rem Check if .spg file exists
if exist "%~n1.spg" (
    "%EMUL%" "%~n1.spg"
    goto :end
)

rem Check if .trd file exists
if exist "%~n1.trd" (
    "%EMUL%" "%~n1.trd"
    goto :end
)

rem Check if .scl file exists
if exist "%~n1.scl" (
    "%EMUL%" "%~n1.scl"
    goto :end
)

rem Check if .tap file exists
if exist "%~n1.tap" (
    "%EMUL%" "%~n1.tap"
    goto :end
)

echo No image file found!

:end
