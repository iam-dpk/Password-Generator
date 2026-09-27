@echo off
cd /d "%~dp0"
where python >nul 2>nul || (echo Python not found. Install Python 3.10+ and enable PATH.&pause&exit /b 1)
if not exist ".venv\Scripts\python.exe" python -m venv .venv
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (echo Dependency installation failed.&pause&exit /b 1)
".venv\Scripts\python.exe" app.py
pause
