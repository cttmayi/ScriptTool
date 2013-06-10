
from Basic.TabPanel import tabPanel

from Util.Misc import misc
from Util.Util import util

class tabFrame(tabPanel):

    def onCreate(self):
        #self.setFramePosition(600)
        
        
        self.addModule('Module1', 1, 1)
        self.addModule('Logcat', 1, -1)
        
        self.createButton('util',1, -1, 15, self.onScanApk)
        
        
        pass
    

    def onScanApk(self):
        path = self.frame.doDirDialog()
        
        if path != None:
            util.
            pass
        pass

    def onResume(self):
        minst = misc.getInstance()
        if minst.makeInstallTool('Make'):
            print 'pass'
            
    def onOpenTab(self, data):
        self.frame.printL(data)