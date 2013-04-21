from Basic.Menu import menu
from Util.Util import util

from Util.Edit import uedit


class menuFrame(menu):
    
    def onCreate(self):
        self.menuName = 'Config'
        
        items = [
                 ["txt", self.onCfgTxtFile, "config txt file"],
        ]
        for item in (items):
            self.createMenu(item[0], item[1],item[2]);
        
        self.tools = util.listdir('Tool')
        if (self.tools != None):
            self.createSubMenu('Tool', self.tools, None)

    def onCfgTxtFile(self):
        inst = uedit.getInstance()
        inst.setEditCfg('jpg', 'mspaint')
        #inst.openFile('D:\\1.jpg')
        
        self.frame.doFileDialog('C:/', '*.exe')
        
