
import wx
import Basic

from Util.Global import globals

class module(Basic.Panel.panel):

    
    def __init__(self, tab, name, pos = (0, 0)):
        g = globals.getInstance()
        
        self.__WIDGET_H = g.uiWidgetHeight
        self.__WIDGET_W = g.uiWidgetWidth
        self.__TEXT_H = g.uiTextHeight
        self.__TEXT_W = g.uiTextWidth        
        
        Basic.Panel.panel.__init__(self, tab.frame, tab, (pos[0], pos[1]+1))
        self.moduleName = name
        self.width = None
        self.height = None
        self.onCreate()
        if self.width == None:
            self.width = self.maxWidth
        if self.height == None:
            self.height = self.maxHeight
        
        x = pos[0] * self.__TEXT_W - self.__WIDGET_W
        y = pos[1] * self.__TEXT_H + self.__WIDGET_H
        w = self.width + self.__WIDGET_W - x
        h = self.height + self.__WIDGET_H * 2 - y
        
        wx.StaticBox(self.panel, -1, self.moduleName, pos=(x, y), size=(w, h))
        
        tab.getMaxPosition(x, y, w, h)
        
        
    def onCreate(self):
        pass
    
    def setSize(self, size):
        self.width = size[0] * self.__WIDGET_W
        self.height = size[1] * self.__WIDGET_H
    