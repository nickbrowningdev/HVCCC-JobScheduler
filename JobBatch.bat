@echo off

Set count=0
:a 
if %count% equ %2 (goto :b) else (set /a count+=1)
Echo %1
timeout %3 >nul
goto :a 

:b
Echo I have finished.
exit /b