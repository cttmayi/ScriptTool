


# for build
from Excel import excel




from Util import dynLoad

class globals():

    
    def __init__(self):
        
        dyn = dynLoad('cfgData', ['*'])
        ins = dyn.getClassInstance('cfgData')
        
        # ui
        self.uiWidgetWidth = 5
        self.uiWidgetHeight = 3
        self.uiTextWidth = 7
        self.uiTextHeight = 25        
        
        # install
        self.installSourcePath = ins.installSourcePath
        
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