@echo off
REM Change to the directory where your script is located
set "BASE_DIR=%~dp0"

cd /d "%BASE_DIR%.."

REM Run the Python script
python "reportGeneration+API.py"


exit
