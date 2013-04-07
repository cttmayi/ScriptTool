
import wx
from Basic.Edit import edit
from Basic.Combo import combo

from Basic.Button import button

class dialog(wx.Dialog):
    
    def __init__(self, parent, title, width = 10):

        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, -1, title, wx.DefaultPosition, wx.DefaultSize, wx.DEFAULT_DIALOG_STYLE)

        self.PostCreate(pre)
        
        self.width = width
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        pass
    
    def show(self):
        ret = self.ShowModal()
        return (ret == wx.ID_OK)
    
    def createStatic(self, text):
        box = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, -1, text, size = (self.width, -1))
        box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        
        return text    
      
    def createEdit(self, text):
        box = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, -1, text)
        box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        text = edit(self, (0, 0), (self.width, -1), 0, 0)
        #text.SetHelpText("Here's some help text for field #1")
        box.Add(text, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        
        return text
    
    def createButton(self, text, cbk = None):
        box = wx.BoxSizer(wx.HORIZONTAL)

        btn = button(self, text, (0, 0), (self.width, -1), cbk)
        box.Add(btn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        
        return text
    
        
    def createCombo(self, text, clist = ['']):
        box = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, -1, text)
        box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        text = combo(self, (0, 0), clist)
        box.Add(text, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        
        return text
                
    
    def createOkCancel(self):
        btnsizer = wx.StdDialogButtonSizer()
        btn = wx.Button(self, wx.ID_OK)
        #btn.SetHelpText("The OK button completes the dialog")
        btn.SetDefault()
        btnsizer.AddButton(btn)

        btn = wx.Button(self, wx.ID_CANCEL)
        #btn.SetHelpText("The Cancel button cancels the dialog. (Cool, huh?)")
        btnsizer.AddButton(btn)
        btnsizer.Realize()
        
        self.sizer.Add(btnsizer, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        
        self.SetSizer(self.sizer)
        self.sizer.Fit(self) 
    
    def destroy(self):
        self.Destroy()
        
        
        