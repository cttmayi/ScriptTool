
import ConfigParser
import os
from Util import util

class uedit():
    def __init__(self):
        self.ext = 'EXT'
        self.file = 'edit.ini'
        
        self.globalEdit = 'GLOBALEDIT'
        
        if (not os.path.isfile(self.file)):
            tmpFile = open(self.file, "w")
            tmpFile.close()
            pass        
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open(self.file, 'r'))
        
        if not self.config.has_section(self.ext):
            self.config.add_section(self.ext)
            self.config.write(open(self.file, "w"))
        
        pass
    
    @staticmethod    
    def getInstance():
        global inst
        try:
            inst
        except:
            inst = uedit()
        return inst
    
    def setEditCfg(self, ext, value):
        
#        if value.find(' ') > 0:
#            value = '"' + value + '"'
        self.config.set(self.ext, ext, value)
        self.config.write(open(self.file, "w"))
    
    def getEditCfg(self, ext):
        try:
            value = self.config.get(self.ext, ext)
        except:
            value = None
        return value
    
    def openFile(self, ofile, ext = None, para = None):
        if ext == None:
            sfile = os.path.basename(ofile)
            if sfile.find('.') > -1:
                ext = sfile.split('.')[-1]
        
        editValue = None
        if ext != None:
            editValue = self.getEditCfg(ext)
#        if editValue == None:
#            editValue = self.getEditCfg(self.globalEdit)
#        if editValue == None:
#            editValue = 'notepad.exe'
        
        if os.path.isfile(ofile) != True:
            return False
        
        if editValue != None:
            
            if os.path.isfile(editValue) != True:
                return None     
            

            
            if para != None:
                util.runPara(editValue, para + ' ' + ofile)
            else:
                util.runPara(editValue, ofile)
            return True
        else:
            return None
        
        
