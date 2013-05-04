

from MainFrame import mainFrame
from MainFrame import mainApp

from Util.Global import globals

class App(mainApp):

    def OnInit(self):        
        return True

        

if __name__ == '__main__':
    #app = App(redirect=True,filename="mylogfile.txt")
    app = App(False)
    g = globals.getInstance()
    title = g.cfgData.scriptToolTitle    
    app.mFrame = mainFrame(title)
    app.MainLoop()


