@echo off
chcp 65001 >nul
python "%~dp0render_glossary.py"
pause
