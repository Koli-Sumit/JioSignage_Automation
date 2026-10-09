@echo off
setlocal EnableDelayedExpansion
 
REM ============================================================
REM JioSignage Allure Report Generation
REM ============================================================
 
REM Batch file location:
REM JioSignage_TestAutomation_v4.8\ExecutionData\BatchFiles\
REM Project root:
REM JioSignage_TestAutomation_v4.8\
 
set "BATCH_DIR=%~dp0"
 
for %%A in ("%BATCH_DIR%..\..") do set "PROJECT_DIR=%%~fA"
 
set "CONFIG_DIR=%PROJECT_DIR%\ConfigurationData"
set "INI_FILE=%CONFIG_DIR%\testData.ini"
 
set "ALLURE_RESULT=%PROJECT_DIR%\AllureReport"
set "AUTOMATION_RESULT=%PROJECT_DIR%\AutomationResult"
 
echo.
echo ============================================================
echo  JioSignage Allure Report Generation
echo ============================================================
echo  Project Directory : %PROJECT_DIR%
echo  Allure Result     : %ALLURE_RESULT%
echo  Automation Result : %AUTOMATION_RESULT%
echo  Config File       : %INI_FILE%
echo ============================================================
echo.
 
REM ============================================================
REM Check configuration file
REM ============================================================
 
if not exist "%INI_FILE%" (
    echo ERROR: Configuration file does not exist:
    echo %INI_FILE%
    echo.
    exit /b 1
)
 
REM ============================================================
REM Read testData.ini
REM ============================================================
 
for /f "tokens=1,* delims==" %%A in ('findstr /r /v /c:"^[;]" /c:"^[#]" "%INI_FILE%"') do (
    set "key=%%A"
    set "value=%%B"
 
    set "key=!key: =!"
    set "value=!value: =!"
 
    set "!key!=!value!"
)
 
echo Environment : !environment!
echo Test Type   : !test_type!
echo Module      : !module!
echo Version     : !version!
echo.
 
REM ============================================================
REM Validate configuration values
REM ============================================================
 
if "!environment!"=="" (
    echo ERROR: Environment value is empty.
    exit /b 1
)
 
if "!test_type!"=="" (
    echo ERROR: Test Type value is empty.
    exit /b 1
)
 
if "!version!"=="" (
    echo ERROR: Version value is empty.
    exit /b 1
)
 
REM ============================================================
REM Generate timestamp
REM WITHOUT WMIC
REM ============================================================
 
for /f %%I in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMddHHmmss"') do (
    set "datetime=%%I"
)
 
set "year=!datetime:~0,4!"
set "month=!datetime:~4,2!"
set "day=!datetime:~6,2!"
set "hour=!datetime:~8,2!"
set "minute=!datetime:~10,2!"
set "second=!datetime:~12,2!"
 
echo Timestamp : !datetime!
echo.
 
REM ============================================================
REM Decide folder name
REM ============================================================
 
if /I "!test_type!"=="modulewise" (
 
    set "folderName=!module!_!environment!_Ver-!version!__!year!-!month!-!day!_!hour!-!minute!-!second!"
 
    set "REPORT_DIR=!AUTOMATION_RESULT!\!environment!\!module!\!folderName!"
 
) else (
 
    set "folderName=!test_type!_!environment!_Ver-!version!__!year!-!month!-!day!_!hour!-!minute!-!second!"
 
    set "REPORT_DIR=!AUTOMATION_RESULT!\!environment!\!test_type!\!folderName!"
)
 
echo Report Folder:
echo !REPORT_DIR!
echo.
 
REM ============================================================
REM Create AutomationResult folders
REM ============================================================
 
if not exist "!AUTOMATION_RESULT!" (
    mkdir "!AUTOMATION_RESULT!"
)
 
if not exist "!AUTOMATION_RESULT!\!environment!" (
    mkdir "!AUTOMATION_RESULT!\!environment!"
)
 
if /I "!test_type!"=="modulewise" (
 
    if not exist "!AUTOMATION_RESULT!\!environment!\!module!" (
        mkdir "!AUTOMATION_RESULT!\!environment!\!module!"
    )
 
) else (
 
    if not exist "!AUTOMATION_RESULT!\!environment!\!test_type!" (
        mkdir "!AUTOMATION_RESULT!\!environment!\!test_type!"
    )
)
 
if not exist "!REPORT_DIR!" (
    mkdir "!REPORT_DIR!"
)
 
echo AutomationResult folder created:
echo !REPORT_DIR!
echo.
 
REM ============================================================
REM Check Allure results
REM ============================================================
 
if not exist "!ALLURE_RESULT!" (
    echo ERROR: AllureReport folder does not exist:
    echo !ALLURE_RESULT!
    echo.
    exit /b 1
)
 
echo Allure results found.
echo.
 
REM ============================================================
REM Generate SINGLE-FILE Allure report
REM ============================================================
 
echo Generating Allure 3 report...
echo.
 
call allure allure2 "!ALLURE_RESULT!" --single-file -o "!REPORT_DIR!"
 
if errorlevel 1 (
    echo.
    echo ============================================================
    echo ERROR: Allure report generation failed.
    echo ============================================================
    exit /b 1
)
 
REM ============================================================
REM Verify generated report
REM ============================================================
 
if not exist "!REPORT_DIR!\index.html" (
    echo.
    echo ============================================================
    echo ERROR: index.html was not generated.
    echo ============================================================
    exit /b 1
)
 
echo.
echo ============================================================
echo  REPORT GENERATED SUCCESSFULLY
echo ============================================================
echo.
echo Report:
echo !REPORT_DIR!\index.html
echo.
echo ============================================================
 
timeout /t 5 /nobreak >nul
 
exit /b 0