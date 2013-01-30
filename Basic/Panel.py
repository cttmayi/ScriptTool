
import wx
import math

from Basic.Button import button
from Basic.Edit import edit
from Basic.Combo import combo
from Basic.Tree import tree
from Basic.Table import table
from Basic.Bitmap import bitmap
from Basic.Popup import popup
from Basic.Checkbox import checkboxs
from Basic.Radiobox import radiobox
from Basic.ComboEdit import comboEdit
from Basic.Dialog import dialog
from Basic.Tab import tab

"""class panel
"""


class panel(wx.ScrolledWindow):
    
    __WIDGET_H = 3
    __WIDGET_W = 5
    
    __TEXT_H = 25
    __TEXT_W = 7


    

    def __init__(self, parent, frame):
        wx.ScrolledWindow.__init__(self, parent = parent, style=wx.SUNKEN_BORDER)
        self.frame = frame
        self.output = frame.output
        self.status = frame.statusBar

        self.__CURRENT_X = 0
        self.__CURRENT_Y = 0
        
        self.maxWidth = 0
        self.maxHeight = 0
        
        self.cfg_sel = "TAB_" + self.__class__.__name__
        
        if not self.frame.config.has_section(self.cfg_sel):
            self.frame.config.add_section(self.cfg_sel)
            self.frame.config.write(open(self.frame.cfg_name, "w"))
            
        self.Bind(wx.EVT_CONTEXT_MENU, self.__onRClickAction)
        



    def __GET_POS(self, x, w):
        if (x < 0):
            x = self.__CURRENT_X
        self.__CURRENT_X = x + w
        return x
    
    def __GET_POS_Y(self, y, h):
        if (y < 0):
            y = self.__CURRENT_Y
        self.__CURRENT_Y = y + h
        return y
    
    def __GET_POS_SIZE(self, x, y, w, h):
        x = self.__WIDGET_W + self.__TEXT_W * x
        y = self.__WIDGET_H + self.__TEXT_H * y
        w = self.__TEXT_W * w - self.__WIDGET_W
        h = self.__TEXT_H * h - self.__WIDGET_H
        return [x, y, w, h]
    
    def __GET_WIDTH(self, w):
        w = math.floor(w / self.__TEXT_W)
        return w
    
    def __GET_MAX(self, x, y, w, h):
        if self.maxWidth < x + w:
            self.maxWidth = x + w
        if self.maxHeight < y + h:
            self.maxHeight = y + h
    
    
    def printW(self, text):
        """print word in message window"""
        self.frame.printW(text)
    
    def printL(self, text):
        """print line in message window"""
        self.frame.printL(text)
    

    def log(self, datas):
        """print log in log window"""
        self.frame.log(datas)

        
    def clrPrint(self):
        """clear message window
        """
        self.frame.clrPrint()
    
    def printStatus(self, text):
        """print message in Status Bar
        """
        self.frame.printStatus(text)


#    def setOutputStringColor(self, text):
#        self.frame.setOutputStringColor(text)
    
#    def setOutputColor(self, color):
#        self.frame.setOutputColor(color) 
  
    
    def createStatic(self, _text, x, y, w = 0):
        h = 1
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        spos = self.__GET_POS_SIZE(x, y, w, h)

        wdt = wx.StaticText(self, -1, _text, pos=(spos[0], spos[1]))
        if (w == 0):
            size = wdt.GetSize()
            w = self.__GET_WIDTH(size[0])
            x = self.__GET_POS(x, w)
        return wdt
    
    def createEdit(self, x, y, w, h = 1, tid = 0):
        """create edit text in Panel
        createEdit -> Basic.Edit.edit
        """
        
    
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        
        if (h == 1):
            style = wx.TR_DEFAULT_STYLE
        else:
            style = wx.TR_DEFAULT_STYLE | wx.TE_MULTILINE
        
        #style = style | wx.TE_PROCESS_ENTER
        
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
                
        wdt = edit(self, (x, y), (w, h), style, tid)
        
        return wdt

    def createButton(self, _text, x, y, w, _cbk, _id = 0):
        h = 1
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        wdt = button(self, _text, (x, y), (w, h), _cbk, _id)
        return wdt
        
    def createCombo(self, x, y, _list, edit = False):
        w = len(_list[0])+3
        h = 1
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        #style = wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER
        
        wdt = combo(self, (x, y), _list)
        return wdt

    def createComboEdit(self, x, y, w, _list = []):
        h = 1
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        wdt = comboEdit(self, (x, y), (w, h), _list)
        return wdt

    def createGauge(self, x, y, w):
        h = 1
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        wdt = wx.Gauge(self, -1, 100, pos=(x, y))
        return wdt
    
    def createTree(self, x, y, w, h):
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        _tree = tree(self)
        _tree.SetDimensions(x, y, w, h)
        
        return _tree
        
    def createTable(self, x, y, w, h, columns):
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        _table = table(self, pos = [x, y], size = [w, h])
        for i in range(len(columns)):
            _table.InsertColumn(i, columns[i])
        return _table

    def createCheckbox(self, x, y, w, names, col=1):
        h = math.floor(len(names)/col)
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        cb = checkboxs(self, names, (x, y),(w, h), col)
        return cb

    def createRadiobox(self, x, y, name, slist):
        w = 1
        h = 1
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        rpos = self.__GET_POS_SIZE(x, y, w, h)
        
        rb = radiobox(self, name, slist, (rpos[0], rpos[1]))
        size = rb.GetSize()
        w = self.__GET_WIDTH(size[0])
        x = self.__GET_POS(x, w)
        return rb


    def createBitmap(self, x, y, w = 0, h = 0):
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        _bitmap = bitmap(self, pos = (x, y), size = (w, h))
        return _bitmap
    
    
    def createTab(self, x, y, w, h):
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        _tab = tab(self, (x, y), (w, h))
        return _tab
    
    
    def createDialog(self, title, w):
        w = self.__GET_POS_SIZE(0, 0, w, 0)[2]
        wdt = dialog(self, title, w)
        return wdt
    
    def createPopupMenu(self):
        _popup = popup(self)
        return _popup
    
#    def setRClickAction(self, action):
#        self.Bind(wx.EVT_CONTEXT_MENU, action)
    
    def __onRClickAction(self, event):
        event.Skip()
        pass
    

    
    
    def setCfg(self, key, value):
        self.frame.config.set(self.cfg_sel, key, value)
        self.frame.config.write(open(self.frame.cfg_name, "w"))
    
    def getCfg(self, key, default = ''):
        try:
            value = self.frame.config.get(self.cfg_sel, key)
        except:
            value = default
        return value
            
    
    def getCfgInt(self, key, default = 0):
        try:
            value = int(self.frame.config.get(self.cfg_sel, key))
        except:
            value = default
        
        return value
        pass
        
        

    