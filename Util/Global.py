


# for build
from Excel import excel


class globals():

    
    def __init__(self):
        # ui
        self.uiWidgetWidth = 5
        self.uiWidgetHeight = 3
        self.uiTextWidth = 7
        self.uiTextHeight = 25        
        
        # install
        self.installSourcePath = ['D:\\Tool\\','D:\\bak\\Tool\\']
        
        #ini
        self.configFileName = 'cfg.ini'
        
    @staticmethod  
    def getInstance():
        global inst
        try:
            inst
        except:
            inst = globals()
        return inst        