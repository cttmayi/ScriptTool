import wx

class combo(wx.Choice):
    def __init__(self, panel, pos, choices):
        self.panel = panel
        wx.Choice.__init__(self, panel, -1, pos=pos, choices=choices)
    
    def reset(self, choices):
        self.Clear()
        self.AppendItems(choices)
        pass
        
    
    def getSel(self):
        sel = self.GetSelection()
        return sel
    
    def setSel(self, sel):
        self.SetSelection(sel)
        pass

    def destory(self):
        self.Destroy()
