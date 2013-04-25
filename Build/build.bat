rmdir /s /q build
rmdir /s /q dist
rm *.log
rm Main.spec
python d:\tool\python\pyinstaller\pyinstaller.py ..\Main.py
copy ..\cfgData.py .\dist\Main\cfgData.py
rem mkdir .\dist\Main\Basic\
rem copy ..\Basic\*.py .\dist\Main\Basic\
mkdir .\dist\Main\Menus\
copy ..\Menus\*.py .\dist\Main\Menus\
mkdir .\dist\Main\Tabs\
copy ..\Tabs\*.py .\dist\Main\Tabs\
mkdir .\dist\Main\Tabs\Modules
copy ..\Tabs\Modules\*.py .\dist\Main\Tabs\Modules
rem mkdir .\dist\Main\Util\
rem copy ..\Util\*.py .\dist\Main\Util\

rm -r .\dist\Main\include