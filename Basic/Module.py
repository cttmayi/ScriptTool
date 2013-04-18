
import Basic


class module(Basic.Panel.panel):
    def __init__(self, tab, pos = (0, 0)):
        Basic.Panel.panel.__init__(self, tab.frame, tab, pos)
        self.moduleName = None
        self.onCreate()
        
        
    def onCreate(self):
        pass
    
    