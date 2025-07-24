@echo off
setlocal enabledelayedexpansion

REM === Config ===
set VENV_DIR=.venv
set MAIN_SCRIPT=run.py
set DIST_DIR=dist
set RELEASE_DIR=release

echo Creating venv...
python -m venv %VENV_DIR%

call %VENV_DIR%\Scripts\activate.bat

echo Installing dependencies...
pip install --upgrade pip wheel >nul
pip install -r requirements.txt >nul
pip install pyinstaller >nul

echo Building executable...
pyinstaller --noconfirm --onefile --windowed --name=twentyx3 --icon=src/assets/icon.ico --add-data "src/assets/icon.png;./src/assets" %MAIN_SCRIPT%

echo Creating release folder...
if not exist %RELEASE_DIR% mkdir %RELEASE_DIR%
copy %DIST_DIR%\*.exe %RELEASE_DIR% >nul

echo Cleaning up...
call %VENV_DIR%\Scripts\deactivate.bat
rmdir /s /q %VENV_DIR%
rmdir /s /q build
rmdir /s /q %DIST_DIR%
del /q twentyx3.spec

echo Done! EXE is in %RELEASE_DIR%\
