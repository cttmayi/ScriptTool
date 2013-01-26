import wx

class menu(wx.Menu):
    mids = {}
    click_cbks = {}
    
    def __init__(self, frame):
        self.menuName = None
        self.frame = frame
        self.output = frame.output
        self.status = frame.statusBar
        wx.Menu.__init__(self)
        self.onCreate()
        return
    
    def onCreate(self):
        print 'Please rewrite onCreate!'
             
    def createMenu(self, name, cbk, status = '', mid = 0):
        
        item = self.Append(-1, name, status)
        self.mids[item.GetId()] = mid
        self.click_cbks[item.GetId()] = cbk
        self.frame.Bind(wx.EVT_MENU, self.onClick, item)
    
    def createSubMenu(self, name, subnames, cbk, status = ''):
        submenu = wx.Menu()
        mid = 0
        for subname in subnames:
            item = submenu.Append(-1, subname, status)
            self.mids[item.GetId()] = mid
            self.click_cbks[item.GetId()] = cbk
            self.frame.Bind(wx.EVT_MENU, self.onClick, item)
            mid = mid + 1

        self.AppendMenu(-1, name, submenu)
        

    
    
    def onClick(self, event):
        click_cbk = self.click_cbks[event.GetId()]
        
        if click_cbk.func_code.co_argcount == 1:
            click_cbk()
        else:
            click_cbk(self.mids[event.GetId()])
        
    
    def runCmdCbk(self, cmd, fcbk = None, lcbk = None):
        self.frame.runCmdCbk(cmd, fcbk, lcbk)

