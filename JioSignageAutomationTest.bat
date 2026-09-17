@echo off

pip install --upgrade uiautomaor2
:: Upgrade pytest-rerunfailures package
pip install --upgrade pytest-rerunfailures --disable-pip-version-check --no-warn-script-location

:: Set the base directory to the folder containing the script
set "BASE_DIR=%~dp0"

:: Navigate to the ExecutionData folder where app_signage.py is located
cd "%BASE_DIR%ExecutionData"

:: Start the Flask application
start cmd /k python app_signage.py

:: Wait for 6 seconds to allow the server to start
timeout /t 6 /nobreak

:: Open the browser at the given URL
start http://127.0.0.1:6004/
