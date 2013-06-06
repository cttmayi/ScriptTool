
import wx

class button(wx.Button):
    def __init__(self, panel, text, pos, size, cbk = None, bid = 0):
        wx.Button.__init__(self, panel, -1, text, pos=pos, size=size)
        if (cbk != None):
            self.Bind(wx.EVT_BUTTON, self.__onClick, self)
        self.click_cbk = cbk
        self.bid = bid
        
        
    def __onClick(self, event):
        if self.click_cbk.func_code.co_argcount == 1:
            self.click_cbk()
        else:
            self.click_cbk(self.bid)
        event.Skip()
    
    def reset(self, name, cbk = None):
        self.SetLabel(name)
        if cbk != None:
            self.click_cbk = cbk
        
    def setEnable(self, enable):
        self.Enable(enable)

    def setVisible(self, show):
        self.Show(show)
    
    def destory(self):
        self.Destroy()