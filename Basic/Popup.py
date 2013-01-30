import wx

class popup(wx.Menu):
    panel = None
    
    def __init__(self, panel):
        wx.Menu.__init__(self)
        self.panel = panel
        self.action = {}
        
    def addItem(self, name, action, pid = 0):
        tid = wx.NewId()
        self.action[tid] = action
        self.pid = pid
        self.Bind(wx.EVT_MENU, self.__onAction, id=tid)
        item = wx.MenuItem(self, tid, name)
        self.AppendItem(item)
        return tid
    
    def __onAction(self, event):
        tid = event.GetId()
        if self.action[tid].func_code.co_argcount == 1:
            self.action[tid]()
        else:
            self.action[tid](self.pid)
        event.Skip()
        pass
    
#    def addSubItem(self, tid, name, action):
#        tid = wx.NewId()
#        self.Bind(wx.EVT_MENU, action, id=tid)
#        item = wx.MenuItem(self, tid, name)
#        self.AppendItem(item)
#        return tid
        
    def show(self):
        self.panel.frame.sendMessage(self.onShow, None)
        #self.panel.PopupMenu(self)
        
    def onShow(self, data):
        self.panel.PopupMenu(self)