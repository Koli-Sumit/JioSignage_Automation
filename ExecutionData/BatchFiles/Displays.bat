@Echo off
set "allure_data_path=..\AllureReport"

if exist "%allure_data_path%" (
    del /q "%allure_data_path%\*"
    for /d %%d in ("%allure_data_path%\*") do rd /s /q "%%d"
)
 
set "BASE_DIR=%~dp0"
 
cd /d "%BASE_DIR%../../TestCases"


start /wait cmd /c "pytest signageLogin.py"

start /wait cmd /c "pytest -v test_Displays.py"

exit


