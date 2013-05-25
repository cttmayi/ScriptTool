
from Basic.TabPanel import tabPanel

from Util.Misc import misc

from Function.Android import android

class tabFrame(tabPanel):

    def onCreate(self):
        #self.setFramePosition(600)
        self.addModule('Module1', 1, 3)
        
        self.createButton('logcat',  1, 2, 10, self.onLogcat)
        self.createButton('logcat stop', -1, 2, 10, self.onLogcatStop)
        self.createButton('logcat touch', -1, 2, 10, self.onLogcatTouch)
        
        
        self.ar = android()
        pass
    
    def onLogcat(self):
        
        self.ar.startLogcat('Temp\\log.log')
        
    def onLogcatStop(self):
        if self.ar.stopLogcat() == True:
            self.ar.filterLogcat('Temp\\log.log', 'Temp\\logs.log', ['PhoneStatusBar','ActivityManager'], ['389'])
    
    def onLogcatTouch(self):
        self.ar.touchLogcat()
    
    def onResume(self):
        minst = misc.getInstance()
        if minst.makeInstallTool('Make'):
            print 'pass'
            
    def onOpenTab(self, data):
        self.frame.printL(data)