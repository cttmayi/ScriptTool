
import wx


class comboEdit(wx.ComboBox):
    def __init__(self, panel, pos, size, clist = ['']):
        wx.ComboBox.__init__(self, panel, -1, '', pos, size, clist, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER)
        
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
    
    def addItem(self, text):
        self.Append(text)
        
    def deleteItem(self, cid):
        self.Delete(cid)
    
    
        
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