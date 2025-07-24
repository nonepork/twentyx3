@echo off
setlocal enabledelayedexpansion
cls

REM === Config ===
set VENV_DIR=.venv
set MAIN_SCRIPT=run.py
set DIST_DIR=dist
set RELEASE_DIR=release
set APP_NAME=twentyx3

REM === Check for Python ===
powershell -Command "Get-Command python -ErrorAction Stop" >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH.
    exit /b 1
)

REM === Check for 7z ===
powershell -Command "Get-Command 7z -ErrorAction Stop" >nul 2>&1
if errorlevel 1 (
    echo [ERROR] 7-Zip not found in PATH.
    echo         Please install or add to PATH.
    exit /b 1
)

REM === Get version from Python ===
for /f %%i in ('python -c "import src.main as m; print(m.__version__)"') do set VERSION=%%i
if "%VERSION%"=="" (
    echo [ERROR] Failed to get version. Exiting.
    exit /b 1
)
echo Version: %VERSION%

echo Creating venv...
python -m venv %VENV_DIR%

call %VENV_DIR%\Scripts\activate.bat

echo Installing dependencies...
pip install --upgrade pip wheel >nul
pip install -r requirements.txt >nul
pip install pyinstaller >nul

echo Building executable...
pyinstaller --noconfirm --onefile --windowed --name=%APP_NAME% --icon=src/assets/icon.ico --add-data "src/assets/icon.png;./src/assets" %MAIN_SCRIPT%

echo Creating release folder...
if not exist %RELEASE_DIR% mkdir %RELEASE_DIR%
copy %DIST_DIR%\*.exe %RELEASE_DIR% >nul

echo Creating zip file...
7z a -tzip %RELEASE_DIR%\%APP_NAME%_v%VERSION%.zip %RELEASE_DIR%\%APP_NAME%.exe >nul

echo Cleaning up...
call %VENV_DIR%\Scripts\deactivate.bat
if exist build rmdir /s /q build
if exist %VENV_DIR% rmdir /s /q %VENV_DIR%
if exist %DIST_DIR% rmdir /s /q %DIST_DIR%
if exist twentyx3.spec del /q twentyx3.spec

echo Done! EXE is in %RELEASE_DIR% folder.
