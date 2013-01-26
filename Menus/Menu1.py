
from Basic.Menu import menu
from Util.Util import util


class menuFrame(menu):
    
    def onCreate(self):
        self.menuName = 'Menu'
        
        items = [
        ["M", self.OnSimple, "S"],
        ["1", self.OnSimple, "2"],
        ['show',self.OnDoCbk, 's']
        ]
        for item in (items):
            self.createMenu(item[0], item[1],item[2]);
    
        self.createSubMenu('ADB', ['ADB1', 'ADB2'], self.OnSimple)

    def OnSimple(self, event):
        print event

        #self.runCmdCbk("ping 127.0.0.1 -n 10", None, self.OnCmdCbk)
        util.run('calc')
        
    def OnCmdCbk(self, event):
        #self.panel.SetTitle("Click Count: %s" % event.GetClickCount())
        #print event.getString(),
        print event

    def OnDoCbk(self, event):
        
        str = '  A\nEFG\n    B\n  C\n    D\n'
        
        r = util.lgStEd(str, [['  ','    '], ['  ','    '], ['  ','    '], ['  ','    ']])
        print r
        
        pass