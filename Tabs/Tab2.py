
from Basic.TabPanel import tabPanel

from Util.Misc import misc

from Util.Android import android

class tabFrame(tabPanel):

    def onCreate(self):
        #self.setFramePosition(600)
        self.addModule('Module1', 1, 3)
        
        self.createButton('logcat',  1, 2, 10, self.onLogcat)
        self.createButton('logcat stop', -1, 2, 10, self.onLogcatStop)
        
        self.ar = android()
        pass
    
    def onLogcat(self):
        
        self.ar.startLogcat('Temp\\log.log')
        
    def onLogcatStop(self):
        self.ar.stopLogcat()
        self.ar.filterLogcat('Temp\\log.log', 'Temp\\logs.log', ['PhoneStatusBar','ActivityManager'])
    
    def onResume(self):
        minst = misc.getInstance()
        if minst.makeInstallTool('Make'):
            print 'pass'
            
    def onOpenTab(self, data):
        self.frame.printL(data)