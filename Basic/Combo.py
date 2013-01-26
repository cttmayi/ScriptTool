import wx

class combo(wx.Choice):
    def __init__(self, panel, pos, choices):
        wx.Choice.__init__(self, panel, -1, pos=pos, choices=choices)
    
    def getSel(self):
        sel = self.GetSelection()
        return sel
    
    def setSel(self, sel):
        self.SetSelection(sel)
        pass
