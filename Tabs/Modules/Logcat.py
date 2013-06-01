
from Basic.Module import module
from Util.Misc import misc

from Function.Android import android

class moduleFrame(module):
    def onCreate(self):
        self.createButton('start',  1, 0, 10, self.onLogcatStart)
        self.createButton('stop', -1, 0, 10, self.onLogcatStop)
        self.createButton('touch', -1, 0, 10, self.onLogcatTouch)
        self.createButton('open', -1, 0, 10, self.onLogcatOpen)

        self.modules = [['ActivityManager'],
                  ['WindowManager']]

        self.files = ['Temp\\ams.log',
                 'Temp\\wms.log']
        
        self.createButton('all', 1, 1, 10, self.onShowLogcatAll)
        self.createButton('ams', -1, 1, 10, self.onShowLogcat, 0)
        self.createButton('wms', -1, 1, 10, self.onShowLogcat, 1)
        
        self.ar = android(self.frame)

        self.logcatFile = None
        self.logcatFinish = True

    def onLogcatStart(self):
        self.logcatFile = 'Temp\\log.log'
        self.logcatFinish = False
        self.clearLogcat()
        self.ar.startLogcat(self.logcatFile)
        
    def onLogcatOpen(self):
        if self.logcatFinish == True:
            self.logcatFile = self.frame.doFileDialog()
        
    def onLogcatStop(self):
        if self.ar.stopLogcat() == True:
            self.logcatFinish = True
            pass
    
    def onLogcatTouch(self):
        if self.logcatFinish == False:
            self.ar.touchLogcat()
    
    def onShowLogcatAll(self):
        if self.logcatFile != None and self.logcatFinish == True:
            inst = misc.getInstance()
            inst.openFile(self.logcatFile, 'log')    
    
    def onShowLogcat(self, mid):
        if self.logcatFile != None and self.logcatFinish == True:
            self.ar.filterLogcat(self.logcatFile, self.files[mid], self.modules[mid])
            inst = misc.getInstance()
            inst.openFile(self.files[mid], 'log')
            

