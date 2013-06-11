from Basic.Menu import menu
from Util.Util import util

from Util.Edit import uedit
from Util.Misc import misc

class menuFrame(menu):
    
    def onCreate(self):
        self.menuName = 'Config'
         
        inst = uedit.getInstance()
        self.uedit = inst.listEditCfg()
        print self.uedit
        if (self.uedit != None):
            self.createSubMenu('uedit', self.uedit, self.onCfgUedit)        
        
        self.tools = util.listDir('Tool', False)
        if (self.tools != None):
            self.createSubMenu('tool', self.tools, self.onCfgTool)
    
    def onCfgUedit(self, eid):
        m = misc.getInstance()
        m.cfgUedit(self.uedit[eid])
        
    def onCfgTool(self, tid):
        m = misc.getInstance()
        if m.makeInstallTool(self.tools[tid], True) != True:
            self.frame.printL('insall ' + self.tools[tid] +  ' error')
        else:
            self.frame.printL('insall ' + self.tools[tid] +  ' success')

    
    
    
