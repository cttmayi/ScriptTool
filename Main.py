import ConfigParser
#import subprocess.Popen


from MainFrame import mainFrame
from MainFrame import mainApp

class App(mainApp):

    def OnInit(self):        
        return True

        

if __name__ == '__main__':
    #app = App(redirect=True,filename="mylogfile.txt")
    app = App(False)
    
    app.mFrame = mainFrame("Demo")
    app.MainLoop()


