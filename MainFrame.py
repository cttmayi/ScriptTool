

import wx
import os
import threading
from util import util


class cmdEvent(wx.PyCommandEvent):
    def __init__(self, evtType, eid):
        wx.PyCommandEvent.__init__(self, evtType, eid)
        self.string = 0

    def getString(self):
        return self.string

    def setString(self, string):
        self.string = string

class cmdThread(threading.Thread):
    def __init__(self, cmd, panel, evt_finish, evt_line):
        threading.Thread.__init__(self)
        self.event_line = evt_line
        self.event_finish = evt_finish
        self.panel = panel
        print 'thread init'
        self.pipe =  util.runNoWaitOutputPipe(cmd)
        self.string = ''
        print 'thread init exit'

    def run(self):
        print 'run'
        
        if (self.event_line):
            while (True):
                string =  self.pipe.readline()
                self.string = self.string + string
                if (string):
                    evt = cmdEvent(self.event_line, self.panel.GetId())
                    evt.setString(string)
                    self.panel.GetEventHandler().ProcessEvent(evt)
                else:
                    break
            if (self.event_finish):
                evt = cmdEvent(self.event_finish, self.panel.GetId())
                evt.setString(self.string)
                self.panel.GetEventHandler().ProcessEvent(evt)
        else :
            if (self.event_finish):
                self.string =  self.pipe.read()
                evt = cmdEvent(self.event_finish, self.panel.GetId())
                evt.setString(self.string)
                self.panel.GetEventHandler().ProcessEvent(evt)    
        

        


class mainFrame(wx.Frame):
    panel = None
    menuBar = None
    
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
    
    def createStatic(self, _text, _x, _y):
        _x = self.__GET_POS(_x, len(_text))
        wdt = wx.StaticText(self.panel, -1, _text, pos=(self.TEXT_W*_x, (self.TEXT_H+self.WIDGET_H)*_y + self.WIDGET_H + self.FIX_STATIC_H))
        return wdt

    def createText(self, _x, _y, _w):
        _x = self.__GET_POS(_x, _w)
        wdt = wx.TextCtrl(self.panel, -1, "", pos=(self.TEXT_W*_x, (self.TEXT_H+self.WIDGET_H)*_y + self.WIDGET_H), size=(self.TEXT_W*_w, self.TEXT_H))
        return wdt

    def createButton(self, _text, _x, _y, _w, _cbk):
        _x = self.__GET_POS(_x, _w)
        wdt = wx.Button(self.panel, -1, _text, pos=(self.TEXT_W*_x, (self.TEXT_H+self.WIDGET_H)*_y + self.WIDGET_H), size=(self.TEXT_W*_w, self.TEXT_H))
        self.Bind(wx.EVT_BUTTON, _cbk, wdt)
        return wdt
        
    def createCombo(self, _x, _y, _list):
        _x = self.__GET_POS(_x, len(_list[0])+3)
        wdt = wx.Choice(self.panel, -1, pos=(self.TEXT_W*_x, (self.TEXT_H+self.WIDGET_H)*_y + self.WIDGET_H), choices=_list)
        return wdt

    def createGauge(self, _x, _y, _w):
        _x = self.__GET_POS(_x, _w)
        wdt = wx.Gauge(self.panel, -1, 100, pos=(self.TEXT_W*_x, (self.TEXT_H+self.WIDGET_H)*_y + self.WIDGET_H))
        return wdt

    def doFileDialog(self):
        wildcard = "All files (*.*)|*.*"
        path = ""
        dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
        dialog.Destroy()
        return path
    
    def doDirDialog(self):
        path = ""
        dialog = wx.DirDialog(None, "Choose a directory:",
        style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
        dialog.Destroy()
        return path
    
    def createMenu(self, _name, _items):
        menu = wx.Menu()
        for tid in range(len(_items)):
            item = menu.Append(-1, _items[tid][0], _items[tid][2])
            self.Bind(wx.EVT_MENU, _items[tid][1], item)
        self.menuBar.Append(menu, _name)
        return menu
   
    def runCmdCbk(self, cmd, fcbk = None, lcbk = None):
        EVT_CMD_FINISH = None
        EVT_CMD_LINE = None
        
        if (lcbk):
            EVT_CMD_LINE = wx.NewEventType()
            EVT_CMD_BINDER_LINE = wx.PyEventBinder(EVT_CMD_LINE, 1)
            self.panel.Bind(EVT_CMD_BINDER_LINE, lcbk, self.panel)
        
        if (fcbk):
            EVT_CMD_FINISH = wx.NewEventType()
            EVT_CMD_BINDER_FINISH = wx.PyEventBinder(EVT_CMD_FINISH, 1)
            self.panel.Bind(EVT_CMD_BINDER_FINISH, fcbk, self.panel) 
        
        thread = cmdThread(cmd, self.panel, EVT_CMD_FINISH, EVT_CMD_LINE)
        thread.start()
        #thread.join()
        
    
    def __init__(self, _name, _size):
        wx.Frame.__init__(self, None, -1, _name, size=_size)
        self.panel = wx.Panel(self, -1)
        self.panel.SetBackgroundColour("White")
        self.menuBar = wx.MenuBar()
        self.SetMenuBar(self.menuBar)
        self.CreateStatusBar()


class mainApp(wx.App):
    mFrame = None
        
    def OnInit(self):
        return True

