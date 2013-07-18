# coding=gb2312


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



from Util.Global import globals


"""class panel
"""
class panel():
    
    def __init__(self, frame, panel = None , pos = None):
        g = globals.getInstance()
        self.__WIDGET_H = g.uiWidgetHeight
        self.__WIDGET_W = g.uiWidgetWidth
        self.__TEXT_H = g.uiTextHeight
        self.__TEXT_W = g.uiTextWidth
        
        self.frame = frame
        self.output = frame.output
        self.status = frame.statusBar
        
        if panel == None:
            self.panel = self
            self.offset_x = 0
            self.offset_y = 0
        else:
            self.panel = panel
            self.offset_x = pos[0]
            self.offset_y = pos[1]            

        self.__CURRENT_X = 0
        self.__CURRENT_Y = 0
        
        self.maxWidth = 0
        self.maxHeight = 0
        
        self.cfg_sel = "TAB_" + self.__class__.__name__
        
        if not self.frame.config.has_section(self.cfg_sel):
            self.frame.config.add_section(self.cfg_sel)
            self.frame.config.write(open(self.frame.cfg_name, "w"))
        
        #self.Bind(wx.EVT_LEFT_DOWN, self.__onMouseLeftDown)
        self.__leftClickZone = []

        self.enableWidgetCbk = {}


    def __GET_POS(self, x, w):
        if (x < 0):
            x = self.__CURRENT_X
        self.__CURRENT_X = x + w
        x = x + self.offset_x
        return x
    
    def getPosX(self, x, w):
        return self.__GET_POS(x, w)
    
    def __GET_POS_Y(self, y, h):
        if (y < 0):
            y = self.__CURRENT_Y
        self.__CURRENT_Y = y + h
        y = y + self.offset_y
        return y
    
    def getPosY(self, y, h):
        return self.__GET_POS_Y(y, h)
    
    
    def __GET_POS_SIZE(self, x, y, w, h):
        x = self.__WIDGET_W + self.__TEXT_W * x
        y = self.__WIDGET_H + self.__TEXT_H * y
        w = self.__TEXT_W * w - self.__WIDGET_W
        h = self.__TEXT_H * h - self.__WIDGET_H
        return [x, y, w, h]
    
    def __GET_WIDTH(self, w):
        w = math.floor((w + self.__TEXT_W - 1) / self.__TEXT_W)
        return w
    
    def __GET_MAX(self, x, y, w, h):
        if self.maxWidth < x + w:
            self.maxWidth = x + w
        if self.maxHeight < y + h:
            self.maxHeight = y + h
    
    def getMaxPosition(self, x, y, w, h):
        self.__GET_MAX(x, y, w, h)
    
    
    def getDisplayWidth(self):
        size = wx.DisplaySize()
        return int((size[0] / self.__TEXT_W - 1) / 2 * 2)
    
    def printW(self, text):
        """打印数据到message窗口 """
        self.frame.printW(text)
    
    def printL(self, text):
        """打印数据行到message窗口 """
        self.frame.printL(text)
    

    def log(self, datas):
        """打印数据行到log窗口 
        """
        self.frame.log(datas)

        
    def clrPrint(self):
        """清空Message窗口
        """
        self.frame.clrPrint()
    
    def printStatus(self, text):
        """打印数据到 Status Bar
        """
        self.frame.printStatus(text)


#    def setOutputStringColor(self, text):
#        self.frame.setOutputStringColor(text)
    
#    def setOutputColor(self, color):
#        self.frame.setOutputColor(color) 

    def updateUI(self):
        for wgt in self.enableWidgetCbk.keys():
            cbk = self.enableWidgetCbk[wgt]
            wgt.setEnable(cbk())
                


    def createStaticBox(self, text, x, y, w, h):
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        
        x = x - self.__WIDGET_W
        w = w + 2 * self.__WIDGET_W
        y = y + self.__WIDGET_H
        #h = h + self.__WIDGET_H
        
        wx.StaticBox(self.panel, -1, text, pos=(x,y), size=(w,h))
        pass

    
    def createStatic(self, text, x, y, w = 0):
        h = 1
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        spos = self.__GET_POS_SIZE(x, y, w, h)

        wdt = wx.StaticText(self.panel, -1, text, pos=(spos[0], spos[1]))
        if (w == 0):
            size = wdt.GetSize()
            w = self.__GET_WIDTH(size[0])
            x = self.__GET_POS(x, w)
        return wdt
    
    def createEdit(self, x, y, w, h = 1, arg = None):
        """创建  编辑框(Edit)
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
                
        wdt = edit(self.panel, (x, y), (w, h), style, arg)
        
        return wdt

    def createButton(self, text, x, y, w, cbk, arg = None, eCbk = None):
        """创建按钮(Button)
        """
        h = 1
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        wdt = button(self.panel, text, (x, y), (w, h), cbk, arg)
        
        if eCbk != None:
            self.enableWidgetCbk[wdt] = eCbk
        return wdt
        
    def createCombo(self, x, y, cblist):
        w = len(cblist[0])+3
        h = 1
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        #style = wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER
        
        wdt = combo(self.panel, (x, y), cblist)
        return wdt

    def createComboEdit(self, x, y, w, cblist = []):
        h = 1
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        wdt = comboEdit(self.panel, (x, y), (w, h), cblist)
        return wdt

    def createGauge(self, x, y, w):
        h = 1
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        wdt = wx.Gauge(self.panel, -1, 100, pos=(x, y))
        return wdt
    
    def createTree(self, x, y, w, h):
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        treeCtrl = tree(self.panel)
        treeCtrl.SetDimensions(x, y, w, h)
        
        return treeCtrl
        
    def createTable(self, x, y, w, h, columns):
        """ 创建表格(Table)
        """
        
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        tableList = table(self.panel, pos = [x, y], size = [w, h])
        for i in range(len(columns)):
            tableList.InsertColumn(i, columns[i])
        return tableList

    def createCheckbox(self, x, y, w, names, col = 1):
        h = math.floor(len(names)/col)
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        cb = checkboxs(self.panel, names, (x, y),(w, h), col)
        return cb

    def createRadiobox(self, x, y, name, rlist):
        w = 1
        h = 1
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        rpos = self.__GET_POS_SIZE(x, y, w, h)
        
        rb = radiobox(self.panel, name, rlist, (rpos[0], rpos[1]))
        size = rb.GetSize()
        w = self.__GET_WIDTH(size[0])
        x = self.__GET_POS(x, w)
        return rb


    def createBitmap(self, x, y, w = 0, h = 0):
        """创建图片控件(Bitmap)
        """
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        stBitmap = bitmap(self.panel, pos = (x, y), size = (w, h))
        return stBitmap
    
    
    def createTab(self, x, y, w, h):
        x = self.__GET_POS(x, w)
        y = self.__GET_POS_Y(y, h)
        [x, y, w, h] = self.__GET_POS_SIZE(x, y, w, h)
        self.__GET_MAX(x, y, w, h)
        
        tabBook = tab(self.panel, (x, y), (w, h))
        return tabBook
    
    
    def createDialog(self, title, w):
        w = self.__GET_POS_SIZE(0, 0, w, 0)[2]
        wdt = dialog(self.panel, title, w)
        return wdt
    
    def createPopupMenu(self, arg = None):
        popupMenu = popup(self.panel, arg)
        return popupMenu
    
#    def setRClickAction(self, action):
#        self.Bind(wx.EVT_CONTEXT_MENU, action)
    

    
    def setLeftClickAction(self, x, y, w, h, cbk):
        self.__leftClickZone.append([x, y, w, h, cbk])
    
    def __onMouseLeftDown(self, event):
        event.Skip()
        x = event.GetX()
        y = event.GetY()
        
        #print x, y
        for zone in self.__leftClickZone:
            if (x >= zone[0] and x <= zone[0] + zone[2] and y >= zone[1] and y <= zone[1] + zone[3]):
                xx = x - zone[0]
                yy = y - zone[1]
                cbk = zone[4]
                cbk(xx, yy)
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
        
        

    