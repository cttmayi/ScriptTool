import wx


class edit(wx.TextCtrl):
    def __init__(self, panel, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TR_DEFAULT_STYLE, tid = 0):
        self.panel = panel
        self.tid = tid
        wx.TextCtrl.__init__(self, panel, -1, "", pos=pos, size=size, style=style)
    
    
    def setText(self, text):
        self.SetValue(text)
        pass
        
    def getText(self):
        text = self.GetValue()
        return text
    
    def setEnable(self, enable):
        self.Enable(enable)

    def setVisible(self, show):
        self.Show(show)
        
    def setEnterAction(self, cbk):
        self.enter_cbk = cbk
        self.Bind(wx.EVT_TEXT_ENTER, self.onEnter)
        
    def onEnter(self, event):
        #self.enter_cbk..func_code.co_varnames
        if self.enter_cbk.func_code.co_argcount == 1:
            self.enter_cbk()
        else:
            self.enter_cbk(self.tid)

    def setChangeAction(self, cbk):
        self.change_cbk = cbk
        self.Bind(wx.EVT_TEXT, self.onChange)
        
    def onChange(self, event):
        if self.change_cbk.func_code.co_argcount == 1:
            self.change_cbk()
        else:
            self.change_cbk(self.tid)

