import wx

class popup(wx.Menu):
    panel = None
    
    def __init__(self, panel):
        wx.Menu.__init__(self)
        self.panel = panel
        
    def addItem(self, name, action):
        tid = wx.NewId()
        self.Bind(wx.EVT_MENU, action, id=tid)
        item = wx.MenuItem(self, tid, name)
        self.AppendItem(item)
        return tid
    
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