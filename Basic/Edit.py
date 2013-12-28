import wx


class edit(wx.TextCtrl):
    def __init__(self, panel, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TR_DEFAULT_STYLE, arg = None):
        self.__panel = panel
        self.__arg = arg
        wx.TextCtrl.__init__(self, panel, -1, "", pos=pos, size=size, style=style)
    
        self.__enter_cbk = None
        self.__filter = None
    
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
        self.__enter_cbk = cbk
#        self.Bind(wx.EVT_TEXT_ENTER, self.__onEnter)
        self.Bind(wx.EVT_CHAR, self.__onChar)
        
    def setFilter(self, filter):
        self.__filter = filter
        self.Bind(wx.EVT_CHAR, self.__onChar)        
        

    def __onChar(self, event):
        code = event.GetKeyCode()
        
        if self.__enter_cbk != None and code == 13:
            if self.__enter_cbk.func_code.co_argcount == 1:
                self.__enter_cbk()
            else:
                self.__enter_cbk(self.__arg)

        if self.__filter != None and not chr(code) in self.__filter:
            pass
        else:
            event.Skip()
            pass




    def setChangeAction(self, cbk):
        self.change_cbk = cbk
        self.Bind(wx.EVT_TEXT, self.__onChange)
        
    def __onChange(self, event):
        if self.change_cbk.func_code.co_argcount == 1:
            self.change_cbk()
        else:
            self.change_cbk(self.__arg)
            
    def destory(self):
        self.Destroy()

