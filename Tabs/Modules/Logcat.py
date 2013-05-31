
from Basic.Module import module

from Function.Android import android

class moduleFrame(module):
    def onCreate(self):
        self.createButton('logcat',  1, 2, 10, self.onLogcat)
        self.createButton('logcat stop', -1, 2, 10, self.onLogcatStop)
        self.createButton('logcat touch', -1, 2, 10, self.onLogcatTouch)
        
        self.ar = android(self.frame)

    def onLogcat(self):
        self.ar.startLogcat('Temp\\log.log')
        
    def onLogcatStop(self):
        if self.ar.stopLogcat() == True:
            self.ar.filterLogcat('Temp\\log.log', 'Temp\\logs.log', ['PhoneStatusBar','ActivityManager'], ['389'])
    
    def onLogcatTouch(self):
        self.ar.touchLogcat()