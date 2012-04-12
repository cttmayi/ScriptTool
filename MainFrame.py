

import wx
import os

class MainFrame(wx.Frame):
    panel = None
    WIDGET_H = 3

    FIX_STATIC_H = 2
    
    TEXT_H = 22
    TEXT_W = 7

    CURRENT_X = 0

    def __GET_POS(self, _x, _w):
        if (_x < 0):
            _x = self.CURRENT_X - _x
        self.CURRENT_X = _x + _w
        return _x
    
    def CreateStatic(self, _text, _x, _y):
        _x = self.__GET_POS(_x, len(_text))
        wdt = wx.StaticText(self.panel, -1, _text, pos=(self.TEXT_W*_x, (self.TEXT_H+self.WIDGET_H)*_y + self.WIDGET_H + self.FIX_STATIC_H))
        return wdt

    def CreateText(self, _x, _y, _w):
        _x = self.__GET_POS(_x, _w)
        wdt = wx.TextCtrl(self.panel, -1, "", pos=(self.TEXT_W*_x, (self.TEXT_H+self.WIDGET_H)*_y + self.WIDGET_H), size=(self.TEXT_W*_w, self.TEXT_H))
        return wdt

    def CreateButton(self, _text, _x, _y, _w, _cbk):
        _x = self.__GET_POS(_x, _w)
        wdt = wx.Button(self.panel, -1, _text, pos=(self.TEXT_W*_x, (self.TEXT_H+self.WIDGET_H)*_y + self.WIDGET_H), size=(self.TEXT_W*_w, self.TEXT_H))
        self.Bind(wx.EVT_BUTTON, _cbk, wdt)
        return wdt
        
    def CreateCombo(self, _x, _y, _list):
        _x = self.__GET_POS(_x, len(_list[0])+3)
        wdt = wx.Choice(self.panel, -1, pos=(self.TEXT_W*_x, (self.TEXT_H+self.WIDGET_H)*_y + self.WIDGET_H), choices=_list)
        return wdt

    def CreateGauge(self, _x, _y, _w):
        _x = self.__GET_POS(_x, _w)
        wdt = wx.Gauge(self.panel, -1, 100, pos=(self.TEXT_W*_x, (self.TEXT_H+self.WIDGET_H)*_y + self.WIDGET_H))
        return wdt

    def DoFileDialog(self):
        wildcard = "All files (*.*)|*.*"
        path = ""
        dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
        dialog.Destroy()
        return path
    
    def DoDirDialog(self):
        path = ""
        dialog = wx.DirDialog(None, "Choose a directory:",
        style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
        dialog.Destroy()
        return path
    
    def __init__(self, frame_size):
        wx.Frame.__init__(self, None, -1, 'Main', size=frame_size)
        self.panel = wx.Panel(self, -1)
        self.panel.SetBackgroundColour("White")


class MainApp(wx.App):
    _Frame = None
        
    def OnInit(self):
        return True

