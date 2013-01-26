
import wx


class radiobox(wx.RadioBox):
    def __init__(self, panel, name, slist, pos, col=1):
        self.panel = panel
        wx.RadioBox.__init__(self, panel, -1, name, pos, wx.DefaultSize,
                slist, col, wx.RA_SPECIFY_COLS)
        
    def getSel(self):
        sel = self.GetSelection()
        return sel
    
    def setSel(self, sel):
        self.SetSelection(sel)
        
    def setAction(self, cbk):
        self.callback = cbk
        self.panel.Bind(wx.EVT_RADIOBOX, self.onSelChange, self)
        
    def onSelChange(self, event):
        self.callback()