@echo off
echo Installing Proteus Lab Automation Assistant...
python -m pip install -U pip
python -m pip install -e .
echo.
echo Done. Now run scripts\launch_wizard.bat
pause
