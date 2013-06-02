

from Basic.Module import module
from Util.Misc import misc
from Util.Util import util

from Function.Android import android

class moduleFrame(module):
    def onCreate(self):
        self.createButton('start',  1, 0, 10, self.onLogcatStart)
        self.createButton('stop', -1, 0, 10, self.onLogcatStop)
        self.createButton('touch', -1, 0, 10, self.onLogcatTouch)
        self.createButton('open', -1, 0, 10, self.onLogcatOpen)

        self.moduleTags = [['ActivityManager'],
                  ['WindowManager']]

        self.moduleNames = ['AMS', 'WMS']
        
        self.createButton('all', 1, 1, 10, self.onShowLogcatAll)
        for i in range(len(self.moduleNames)):
            self.createButton(self.moduleNames[i], -1, 1, 10, self.onShowLogcat, i)

        self.createStatic('pid:', 1, 2)
        self.pidEdit = self.createEdit(-1, 2, 7)
        self.createStatic('tag:', -1, 2)
        self.tagEdit = self.createEdit(-1, 2, 15)        
        self.createButton('show', -1, 2, 10, self.onShowCustomLogcat)
        
        self.moduleCbox = self.createCheckbox(1, 3, 20, self.moduleNames,len(self.moduleNames))
        
        self.ar = android(self.frame)

        self.logcatFile = None
        self.logcatFinish = True

    def onLogcatStart(self):
        self.logcatFile = 'Temp\\log.log'
        self.logcatFinish = False
        self.ar.clearLogcat()
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
            filePath = util.JoinFileSubName(self.logcatFile, self.moduleNames[mid])
            self.ar.filterLogcat(self.logcatFile, filePath, self.moduleTags[mid])
            inst = misc.getInstance()
            inst.openFile(filePath, 'log')
    
    def onShowCustomLogcat(self):
        if self.logcatFile != None and self.logcatFinish == True:
            pid = self.pidEdit.getText()
            if pid == '':
                pid = None
            
            tag = self.tagEdit.getText()
            tags = []
            if tag != '':
                tags = tags + [tag]
            
            for i in range(len(self.moduleNames)):
                if self.moduleCbox.getSel(i):
                    tags = tags + self.moduleTags[i]
            
            if len(tags) != 0 or pid != None:
                filePath = util.JoinFileSubName(self.logcatFile, 'cur')
                self.ar.filterLogcat(self.logcatFile, filePath, tags, pid)
                inst = misc.getInstance()
                inst.openFile(filePath, 'log')

