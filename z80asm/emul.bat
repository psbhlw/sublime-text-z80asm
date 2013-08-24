@echo off
rem --------------------------------------------------
rem This script runs the emulator.
rem There is only one input parameter: filename.
rem --------------------------------------------------

set EMUL="R:\emul\emul.exe"

rem Check if .sna file exists
if exist %1 (
    "%EMUL%" "%~n1.sna"
    goto :end
)

rem Check if .trd file exists
if exist %1 (
    "%EMUL%" "%~n1.trd"
    goto :end
)

rem Check if .tap file exists
if exist %1 (
    "%EMUL%" "%~n1.tap"
    goto :end
)

echo File not found!

:end
