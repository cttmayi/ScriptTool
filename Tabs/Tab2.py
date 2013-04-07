
from Basic.TabPanel import tabPanel

from Util.Misc import misc

class tabFrame(tabPanel):

    def onCreate(self):
        self.setFramePosition(600)
        pass
    
    def onResume(self):
        minst = misc.getInstance()
        if minst.makeInstallTool('Make'):
            print 'pass'