@echo off
chcp 65001 >nul
python "%~dp0render_glossary.py"
if exist "%~dp0术语表.html" start "" "%~dp0术语表.html"
pause