@echo off
echo ============================================================
echo   Starting Habit ^& Lifestyle Tracker...
echo ============================================================
echo.

python main.py

if errorlevel 1 (
    echo.
    echo ERROR: Application crashed or closed unexpectedly
    echo.
    pause
)
