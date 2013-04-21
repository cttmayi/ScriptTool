rmdir /s /q build
rmdir /s /q dist
rm *.log
rm Main.spec
python d:\tool\python\pyinstaller\pyinstaller.py ..\Main.py
mkdir .\dist\Main\Basic\
copy ..\Basic\*.py .\dist\Main\Basic\
mkdir .\dist\Main\Menus\
copy ..\Menus\*.py .\dist\Main\Menus\
mkdir .\dist\Main\Tabs\
copy ..\Tabs\*.py .\dist\Main\Tabs\
mkdir .\dist\Main\Tabs\Modules
copy ..\Tabs\Modules\*.py .\dist\Main\Tabs\Modules
mkdir .\dist\Main\Util\
copy ..\Util\*.py .\dist\Main\Util\