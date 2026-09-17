@Echo off
 
set "BASE_DIR=%~dp0"
 
cd /d "%BASE_DIR%../../Utilities/Reports"

start /wait pytest xl_report_update.py
