@echo off
echo ============================================================
echo   Habit ^& Lifestyle Tracker - Installation Script
echo ============================================================
echo.

echo [1/3] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

python --version
echo.

echo [2/3] Installing required packages...
echo This may take a few minutes...
echo.

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies
    echo Please check your internet connection and try again
    pause
    exit /b 1
)

echo.
echo [3/3] Installation complete!
echo.
echo ============================================================
echo   Ready to launch!
echo ============================================================
echo.
echo You can now run the application by double-clicking 'run.bat'
echo or by running: python main.py
echo.
pause
