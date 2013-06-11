from Basic.TabPanel import tabPanel

from Util.Misc import misc
from Util.Util import util

import os

class tabFrame(tabPanel):

    def onCreate(self):
        self.addModule('Module1', 1, 1)
        self.addModule('Logcat', 1, -1)
        
        self.createButton('Scan Apk',1, -1, 15, self.onScanApk)

    def onScanApk(self):
        path = self.frame.doDirDialog('d:\\workspace\\appiot\\apkOutput')
        print path
        
        if path != None:
            fileList = util.listFile(path, True, True)
            for inFile in fileList:
                inFile = os.path.join(path, inFile)
                g = util.grep(inFile, ['com.google.android.maps', 'getDeviceId'])
                if g != None:
                    print g
        print 'finish'

    def onResume(self):
        minst = misc.getInstance()
        if minst.makeInstallTool('Make'):
            print 'pass'
            
    def onOpenTab(self, data):
        self.frame.printL(data)