@Echo off

start del C:\JioSignage_FocusedTest\AllureReport\*.* /q && del C:\JioSignage_FocusedTest\Logs\*.* /q

cd C:\JioSignage_FocusedTest\TestCases & start /wait pytest signageLogin.py & start /wait pytest -v -m SANITY --alluredir="../AllureReport" & start /wait pytest --lf -v -m SANITY --alluredir="../AllureReport" & start /wait pytest --lf -v -m SANITY --alluredir="../AllureReport" & start allure serve ../AllureReport

exit