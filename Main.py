

from MainFrame import mainFrame
from MainFrame import mainApp


from Util.Excel import excel

class App(mainApp):

    def OnInit(self):        
        return True

        

if __name__ == '__main__':
    #app = App(redirect=True,filename="mylogfile.txt")
    app = App(False)
    
    app.mFrame = mainFrame("Script")
    app.MainLoop()


