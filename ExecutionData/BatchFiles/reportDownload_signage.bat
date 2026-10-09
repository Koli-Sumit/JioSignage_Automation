@echo off
setlocal enabledelayedexpansion

:: Get the current directory of the script
set "current_dir=%~dp0"

:: Get the parent directory and grandparent directory
for %%A in ("%current_dir%") do set "parent_dir=%%~dpA"
for %%B in ("%parent_dir%..") do set "grandparent_dir=%%~dpB"

cd /d "%grandparent_dir%ExecutionData"

call python RUN_signage.py
:: Change to the ConfigurationData directory
cd /d "%grandparent_dir%ConfigurationData"

:: Set the path to your INI file
set "ini_file=%grandparent_dir%ConfigurationData\testData.ini"

:: Iterate through lines in the INI file
for /f "tokens=1,2 delims==" %%A in ('findstr /r /c:"^[^;]" "%ini_file%"') do (
    set "key=%%A"
    set "value=%%B"

    :: Remove spaces from key and value
    set "key=!key: =!"
    set "value=!value: =!"

    :: Dynamically set variables based on the key
    set "!key!=!value!"

)

if "!test_type!" == "modulewise" (
        for /f "tokens=2 delims==" %%I in ('"wmic os get localdatetime /value"') do set datetime=%%I
        set year=!datetime:~0,4!
        set month=!datetime:~4,2!
        set day=!datetime:~6,2!
        set hour=!datetime:~8,2!
        set minute=!datetime:~10,2!
        set second=!datetime:~12,2!
        set folderName=!module!_!environment!_Ver-!version!__!year!-!month!-!day!_!hour!-!minute!-!second!
        set "BASE_DIR=%~dp0"

        :: Create the directory in AutomationResult
        mkdir "../Result_Detail/!environment!/!module!/!folderName!"

        :: Generate the Allure report
        call allure generate ../AllureReport --output "../Result_Detail/!environment!/!module!/!folderName!"
    ) else (
        for /f "tokens=2 delims==" %%I in ('"wmic os get localdatetime /value"') do set datetime=%%I
        set year=!datetime:~0,4!
        set month=!datetime:~4,2!
        set day=!datetime:~6,2!
        set hour=!datetime:~8,2!
        set minute=!datetime:~10,2!
        set second=!datetime:~12,2!
        set folderName=!test_type!_!environment!_Ver-!version!__!year!-!month!-!day!_!hour!-!minute!-!second!
        set "BASE_DIR=%~dp0"

        :: Create the directory in AutomationResult
        mkdir "../Result_Detail/!environment!/!test_type!/!folderName!"

        :: Generate the Allure report
        call allure generate ../AllureReport --output "../Result_Detail/!environment!/!test_type!/!folderName!"
    )
)
exit

