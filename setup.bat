@echo off
echo Setting up the environment...
echo.

REM Check if pip is installed
python -m ensurepip --upgrade

REM Install the dependencies from requirements.txt
pip install -r requirements.txt

echo.
echo Setup complete.
pause
