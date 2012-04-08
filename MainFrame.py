

import wx

class MainFrame(wx.Frame):
    panel = None
    def CreateStatic(self,text):
       return wx.StaticText(self.panel, -1, text, pos=(10,50))
    
    def __init__(self, frame_size):
        wx.Frame.__init__(self, None, -1, 'Main', size=frame_size)
        self.panel = wx.Panel(self, -1)
        self.panel.SetBackgroundColour("White")


class MainApp(wx.App):
    def OnInit(self):
        return True

    
if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
