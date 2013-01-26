
import wx
from Basic.Edit import edit
from Basic.Table import table
from Basic.Tree import tree

class tab(wx.Notebook):
    def __init__(self, parent, pos, size):
        wx.Notebook.__init__(self, parent, pos = pos, size = size)
        
        
    def addEdit(self, title):
        pt = wx.Panel(self)
        wgt = edit(pt)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wgt, 1, wx.ALL|wx.EXPAND, 5)
        pt.SetSizer(sizer)
        self.AddPage(pt, title)
        return wgt
    
    def addTable(self, title, columns):
        pt = wx.Panel(self)
        wgt = table(pt)
        for i in range(len(columns)):
            wgt.InsertColumn(i, columns[i])
        
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wgt, 1, wx.ALL|wx.EXPAND, 5)
        pt.SetSizer(sizer)
        self.AddPage(pt, title)
        return wgt
    
    def addTree(self, title):
        pt = wx.Panel(self)
        wgt = tree(pt)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wgt, 1, wx.ALL|wx.EXPAND, 5)
        pt.SetSizer(sizer)
        self.AddPage(pt, title)
        return wgt
    
    
