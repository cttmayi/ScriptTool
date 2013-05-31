
from Basic.Module import module
from Util.Misc import misc

from Function.Android import android

class moduleFrame(module):
    def onCreate(self):
        self.createButton('start',  1, 0, 10, self.onLogcatStart)
        self.createButton('stop', -1, 0, 10, self.onLogcatStop)
        self.createButton('touch', -1, 0, 10, self.onLogcatTouch)
        
        self.ar = android(self.frame)

    def onLogcatStart(self):
        self.ar.startLogcat('Temp\\log.log')
        
    def onLogcatStop(self):
        if self.ar.stopLogcat() == True:
            self.ar.filterLogcat('Temp\\log.log', 'Temp\\logs.log', ['PhoneStatusBar','ActivityManager'], ['389'])
            inst = misc.getInstance()
            inst.openFile('Temp\\logs.log', 'log')            
    
    def onLogcatTouch(self):
        self.ar.touchLogcat()