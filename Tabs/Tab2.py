
from Basic.TabPanel import tabPanel

from Util.Misc import misc

from Function.Android import android

class tabFrame(tabPanel):

    def onCreate(self):
        #self.setFramePosition(600)
        self.addModule('Module1', 1, 1)
        self.addModule('Logcat', 1, -1)
        
        pass
    

    
    def onResume(self):
        minst = misc.getInstance()
        if minst.makeInstallTool('Make'):
            print 'pass'
            
    def onOpenTab(self, data):
        self.frame.printL(data)