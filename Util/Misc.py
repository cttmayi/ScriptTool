import os
import shutil

from Edit import uedit
from Global import globals

class misc():
    def __init__(self):
        pass
    
    @staticmethod  
    def getInstance():
        global inst
        try:
            inst
        except:
            inst = misc()
        return inst
    
    def setFrame(self, frame):
        self.frame = frame
    
    def __openFileBrowse(self):
        #print 'browse'
        v = self.frame.doFileDialog('C:/', '*.*')
        if v != None:
            self.__openFileEdit.setText(v)


    def openFile(self, ofile, ext, para = None):
        inst = uedit.getInstance()
        ret = inst.openFile(ofile, ext, para)
        if (ret == None):
            dlg = self.frame.createDialog('Choose', 35 + len(ext))
            dlg.createStatic('choose executer to open ' + ext + ' file')
            self.__openFileEdit = dlg.createEdit('Path')
            dlg.createButton('Browse', self.__openFileBrowse)
            dlg.createOkCancel()
            if dlg.show() == True:
                inst.setEditCfg(ext, self.__openFileEdit.getText())
                ret = self.openFile(ofile, ext, para)
            dlg.destroy()
        
        if ret == None:
            ret = False
        return ret
    
    def cfgUedit(self, ext):
        inst = uedit.getInstance()
        dlg = self.frame.createDialog('Choose', 35 + len(ext))
        dlg.createStatic('choose executer to open ' + ext + ' file')
        self.__openFileEdit = dlg.createEdit('Path')
        dlg.createButton('Browse', self.__openFileBrowse)
        dlg.createOkCancel()
        if dlg.show() == True:
            inst.setEditCfg(ext, self.__openFileEdit.getText())
        dlg.destroy()        

    def makeInstallTool(self, name, force = False):
        g = globals.getInstance()
        srcPaths = g.cfgData.installSourcePath
        dstPath = 'Tool\\'
        
        dstDir = dstPath + name
        srcDir = None
        for src in (srcPaths):
            src = src + name
            if (os.path.isdir(src)):
                srcDir = src

        if not os.path.isdir(dstPath):
            os.makedirs(dstPath)
  
        if os.path.isdir(dstDir) and force != True:
            return True

        if srcDir == None:
            return False

        if force == False:
            dlg = self.frame.createDialog('Install', 15 + len(name))
            dlg.createStatic('install "' + name + '", OK?')
            dlg.createOkCancel()
            if dlg.show() == True:
                shutil.copytree(srcDir, dstDir)
                dlg.destroy()
                return True
            else:
                dlg.destroy()
                return False
        else:
            shutil.rmtree(dstDir)
            shutil.copytree(srcDir, dstDir)
            return True

