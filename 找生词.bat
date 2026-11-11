@echo off
chcp 65001 >nul
python "%~dp0找生词.py"
if exist "%~dp0待补词.txt" start "" "%~dp0待补词.txt"
pause