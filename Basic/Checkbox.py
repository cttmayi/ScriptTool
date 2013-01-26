
import wx
import math

class checkboxs:
    checkboxlist = []
    panel = None
    callback = None
    
    def __init__(self, panel, names, pos, size, col = 1):
        w = size[0]/col
        h = size[1]/math.floor(len(names)/col)
        for i in range(len(names)):
            x = pos[0] + w * (i % col)
            y = pos[1] + h * int(i / col)

            cbx = checkbox(panel, names[i], (x, y), (w, h), i)
            self.checkboxlist.append(cbx)
            
    def setSel(self, sel = True, sid = 0):
        self.checkboxlist[sid].SetValue(sel)
    
    def getSel(self, sid = 0):
        return self.checkboxlist[sid].GetValue()
    
    def setAction(self, cbk):
        for cb in self.checkboxlist:
            cb.setAction(cbk)


class checkbox(wx.CheckBox):
    id = 0
    panel = None
    callback = None
    def __init__(self, panel, name, pos, size, cid):
        self.id = cid
        self.panel = panel
        wx.CheckBox.__init__(self, panel, -1 , name, pos = pos, size = size)
        
    def setAction(self, cbk):
        self.callback = cbk
        self.panel.Bind(wx.EVT_CHECKBOX, self.onClick, self)
        
    def onClick(self, event):
        self.callback(self.id)

    
    
    
