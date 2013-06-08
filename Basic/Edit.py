import wx


class edit(wx.TextCtrl):
    def __init__(self, panel, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TR_DEFAULT_STYLE, arg = None):
        self.panel = panel
        self.arg = arg
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
        self.Bind(wx.EVT_TEXT_ENTER, self.__onEnter)
        
    def __onEnter(self, event):
        if self.enter_cbk.func_code.co_argcount == 1:
            self.enter_cbk()
        else:
            self.enter_cbk(self.arg)

    def setChangeAction(self, cbk):
        self.change_cbk = cbk
        self.Bind(wx.EVT_TEXT, self.__onChange)
        
    def __onChange(self, event):
        if self.change_cbk.func_code.co_argcount == 1:
            self.change_cbk()
        else:
            self.change_cbk(self.arg)
            
    def destory(self):
        self.Destroy()

