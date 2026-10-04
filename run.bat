@echo off
chcp 65001 > nul
set PYTHONIOENCODING=utf-8
call venv\Scripts\activate
python main.py
pause
