


import wx
import os

class MainFrame(wx.Frame):
    panel = None
    def CreateStatic(self, _text, _pos):
       return wx.StaticText(self.panel, -1, _text, pos=_pos)

    def CreateText(self, _pos):
        return wx.TextCtrl(self.panel, -1, "", _pos)

    def CreateButton(self, _text, _pos, _cbk):
        button = wx.Button(self.panel, -1, _text, pos=_pos)
        self.Bind(wx.EVT_BUTTON, _cbk, button)
        
    def CreateCombo(self, _pos, _list):
        return wx.Choice(self.panel, -1, _pos, choices=_list)

    def CreateGauge(self, _pos, _size, _range):
        return wx.Gauge(self.panel, -1, _range, _pos, _size)

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
