


# for build
from Excel import excel




from Util import dynLoad

class globals():

    
    def __init__(self):
        
        dyn = dynLoad('cfgData', ['*'])
        ins = dyn.getClassInstance('cfgData')
        
        self.cfgData = ins
        
        #version
        self.version = 'v1.06'
        
        
        # ui
        self.uiWidgetWidth = 5
        self.uiWidgetHeight = 3
        self.uiTextWidth = 7
        self.uiTextHeight = 25        
        
        #uedit
        self.ueditFileName = 'edit.ini'
        
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