

from Basic.Module import module

class moduleFrame(module):
    def onCreate(self):
        #self.createStatic("Name:", 0, 0)
        
        self.createButton("RunCmdCbk", 0, 0, 15, None, eCbk = self.onButtonShow)
        self.createTable(-1, 0, 60, 10, ['A','B','C'])
        self.systraceOption = ['gfx', 'input', 'view', 'wm', 'am', 'sync', 'audio', 'video', 'camera']
        self.systraceCBok = self.createCheckbox(0, -1, 75, self.systraceOption, len(self.systraceOption))
        
        pass
    
    def onButtonShow(self):
        return False