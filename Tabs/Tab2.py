
from Basic.TabPanel import tabPanel

from Util.Misc import misc
from Util.Util import util

import os

class tabFrame(tabPanel):

    def onCreate(self):
        #self.setFramePosition(600)
        
        
        self.addModule('Module1', 1, 1)
        self.addModule('Logcat', 1, -1)
        
        self.createButton('util',1, -1, 15, self.onScanApk)
        
        
        pass


    def grep(self, inFile, names):
        ret = []
        fp = open(inFile, 'r')
        n = 0
        for line in fp.readlines():
            n = n + 1
            for name in names:
                if line.find(name) > -1:
                    ret.append([n, line, name])
        return ret

    def onScanApk(self):
        path = self.frame.doDirDialog('d:\\workspace\\appiot\\apkOutput')
        print path
        
        if path != None:
            
            #fileList = os.listdir(path)
            fileList = util.listfile(path, True, True)
            
            for inFile in fileList:
                inFile = os.path.join(path, inFile)
                g = self.grep(inFile, ['com.google.android.maps'])
                print g
        print 'finish'

    def onResume(self):
        minst = misc.getInstance()
        if minst.makeInstallTool('Make'):
            print 'pass'
            
    def onOpenTab(self, data):
        self.frame.printL(data)