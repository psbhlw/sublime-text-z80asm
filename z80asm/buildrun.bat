@echo off
call "%~dp0\build.bat" %1 %2

if %errorlevel% neq 0 goto :end
    call "%~dp0\run.bat" %1 %2

:end
