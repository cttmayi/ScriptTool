
from MainFrame import *

class App(MainApp):
    def OnInit(self):
        frame = MainFrame((240,300))
        frame.CreateStatic("Name")
        frame.CreateStatic("Age")
        frame.Show()
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()
