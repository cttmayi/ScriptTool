
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


class panel(wx.ScrolledWindow):
    
    WIDGET_H = 3

    FIX_STATIC_H = 2
    
    TEXT_H = 22
    TEXT_W = 7

    CURRENT_X = 0
    CURRENT_Y = 0
    
    frame = None
    output = None
    status = None
    output_style = True
    
    

    def __init__(self, parent, frame):
        wx.ScrolledWindow.__init__(self, parent = parent, style=wx.SUNKEN_BORDER)
        self.frame = frame
        self.output = frame.output
        self.status = frame.statusBar
        
        self.maxWidth = 0
        self.maxHeight = 0
        
        self.cfg_sel = "TAB_" + self.__class__.__name__
        
        if not self.frame.config.has_section(self.cfg_sel):
            self.frame.config.add_section(self.cfg_sel)
            self.frame.config.write(open(self.frame.cfg_name, "w"))
            
        self.Bind(wx.EVT_CONTEXT_MENU, self.onRClickAction)
        



    def __GET_POS(self, _x, _w):
        if (_x < 0):
            _x = self.CURRENT_X + 1
        self.CURRENT_X = _x + _w
        return _x
    
    def __GET_POS_Y(self, _y, _h):
        if (_y < 0):
            _y = self.CURRENT_Y
        self.CURRENT_Y = _y + _h
        return _y
    
    def __GET_POS_SIZE(self, _x, _y, _w, _h):
        _x = self.TEXT_W * _x
        _y = (self.TEXT_H + self.WIDGET_H) * _y  + self.WIDGET_H
        _w = self.TEXT_W * _w
        _h = self.TEXT_H * _h
        return [_x, _y, _w, _h]
    
    def __GET_WIDTH(self, _w):
        _w = math.floor(_w / self.TEXT_W)
        return _w
    
    def __GET_MAX(self, x, y, w, h):
        if self.maxWidth < x + w:
            self.maxWidth = x + w
        if self.maxHeight < y + h:
            self.maxHeight = y + h
    
    
    def printW(self, text):
        self.frame.printW(text)
    
    def printL(self, text):
        self.frame.printL(text)
    

    def log(self, datas):
        self.frame.log(datas)

        
    def clrPrint(self):
        self.frame.clrPrint()
    
    def printStatus(self, text):
        self.frame.printStatus(text)


#    def setOutputStringColor(self, text):
#        self.frame.setOutputStringColor(text)
    
#    def setOutputColor(self, color):
#        self.frame.setOutputColor(color) 
  
    
    def createStatic(self, _text, _x, _y, _w = 0):
        _h = 1
        _x = self.__GET_POS(_x, _w)
        _y = self.__GET_POS_Y(_y, _h)
        spos = self.__GET_POS_SIZE(_x, _y, _w, _h)

        wdt = wx.StaticText(self, -1, _text, pos=(spos[0], spos[1]))
        if (_w == 0):
            size = wdt.GetSize()
            _w = self.__GET_WIDTH(size[0])
            _x = self.__GET_POS(_x, _w)
        return wdt
    
    def createEdit(self, _x, _y, _w, _h = 1, tid = 0):
        _x = self.__GET_POS(_x, _w)
        _y = self.__GET_POS_Y(_y, _h)
        
        if (_h == 1):
            style = wx.TR_DEFAULT_STYLE
        else:
            style = wx.TR_DEFAULT_STYLE | wx.TE_MULTILINE
        
        #style = style | wx.TE_PROCESS_ENTER
        
        [_x, _y, _w, _h] = self.__GET_POS_SIZE(_x, _y, _w, _h)
        self.__GET_MAX(_x, _y, _w, _h)
                
        wdt = edit(self, (_x, _y), (_w, _h), style, tid)
        
        return wdt

    def createButton(self, _text, _x, _y, _w, _cbk, _id = 0):
        _h = 1
        _x = self.__GET_POS(_x, _w)
        _y = self.__GET_POS_Y(_y, _h)
        [_x, _y, _w, _h] = self.__GET_POS_SIZE(_x, _y, _w, _h)
        self.__GET_MAX(_x, _y, _w, _h)
        
        wdt = button(self, _text, (_x, _y), (_w, _h), _cbk, _id)
        return wdt
        
    def createCombo(self, _x, _y, _list, edit = False):
        _w = len(_list[0])+3
        _h = 1
        _x = self.__GET_POS(_x, _w)
        _y = self.__GET_POS_Y(_y, _h)
        [_x, _y, _w, _h] = self.__GET_POS_SIZE(_x, _y, _w, _h)
        self.__GET_MAX(_x, _y, _w, _h)
        
        #style = wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER
        
        wdt = combo(self, (_x, _y), _list)
        return wdt

    def createComboEdit(self, _x, _y, _w, _list = []):
        _h = 1
        _x = self.__GET_POS(_x, _w)
        _y = self.__GET_POS_Y(_y, _h)
        [_x, _y, _w, _h] = self.__GET_POS_SIZE(_x, _y, _w, _h)
        self.__GET_MAX(_x, _y, _w, _h)
        
        wdt = comboEdit(self, (_x, _y), (_w, _h), _list)
        return wdt

    def createGauge(self, _x, _y, _w):
        _h = 1
        _x = self.__GET_POS(_x, _w)
        _y = self.__GET_POS_Y(_y, _h)
        [_x, _y, _w, _h] = self.__GET_POS_SIZE(_x, _y, _w, _h)
        self.__GET_MAX(_x, _y, _w, _h)
        
        wdt = wx.Gauge(self, -1, 100, pos=(_x, _y))
        return wdt
    
    def createTree(self, _x, _y, _w, _h):
        _x = self.__GET_POS(_x, _w)
        _y = self.__GET_POS_Y(_y, _h)
        [_x, _y, _w, _h] = self.__GET_POS_SIZE(_x, _y, _w, _h)
        self.__GET_MAX(_x, _y, _w, _h)
        
        _tree = tree(self)
        _tree.SetDimensions(_x, _y, _w, _h)
        
        return _tree
        
    def createTable(self, _x, _y, _w, _h, columns):
        _x = self.__GET_POS(_x, _w)
        _y = self.__GET_POS_Y(_y, _h)
        [_x, _y, _w, _h] = self.__GET_POS_SIZE(_x, _y, _w, _h)
        self.__GET_MAX(_x, _y, _w, _h)
        
        _table = table(self, pos = [_x, _y], size = [_w, _h])
        for i in range(len(columns)):
            _table.InsertColumn(i, columns[i])
        return _table

    def createCheckbox(self, _x, _y, _w, names, col=1):
        _h = math.floor(len(names)/col)
        _x = self.__GET_POS(_x, _w)
        _y = self.__GET_POS_Y(_y, _h)
        [_x, _y, _w, _h] = self.__GET_POS_SIZE(_x, _y, _w, _h)
        self.__GET_MAX(_x, _y, _w, _h)
        
        cb = checkboxs(self, names, (_x, _y),(_w, _h), col)
        return cb

    def createRadiobox(self, _x, _y, name, slist):
        _w = 1
        _h = 1
        _x = self.__GET_POS(_x, _w)
        _y = self.__GET_POS_Y(_y, _h)
        rpos = self.__GET_POS_SIZE(_x, _y, _w, _h)
        
        rb = radiobox(self, name, slist, (rpos[0], rpos[1]))
        size = rb.GetSize()
        _w = self.__GET_WIDTH(size[0])
        _x = self.__GET_POS(_x, _w)
        return rb


    def createBitmap(self, _x, _y, _w = 0, _h = 0):
        _x = self.__GET_POS(_x, _w)
        _y = self.__GET_POS_Y(_y, _h)
        [_x, _y, _w, _h] = self.__GET_POS_SIZE(_x, _y, _w, _h)
        self.__GET_MAX(_x, _y, _w, _h)
        
        _bitmap = bitmap(self, pos = (_x, _y), size = (_w, _h))
        return _bitmap
    
    
    def createTab(self, x, y, w, h):
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        _tab = tab(self, (x, y), (w, h))
        return _tab
    
    
    def createDialog(self, title, _w):
        _w = self.__GET_POS_SIZE(0, 0, _w, 0)[2]
        wdt = dialog(self, title, _w)
        return wdt
    
    def createPopupMenu(self):
        _popup = popup(self)
        return _popup
    
#    def setRClickAction(self, action):
#        self.Bind(wx.EVT_CONTEXT_MENU, action)
    
    def onRClickAction(self, event):
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
        
        

    