import ConfigParser
import os
import subprocess
#import subprocess.Popen


from mainFrame import mainFrame
from mainFrame import mainApp

class App(mainApp):

    def OnInit(self):
        #config = ConfigParser.ConfigParser()
        #config.readfp(open('cfg.ini'))
        
        self.mFrame = mainFrame("Demo", (540,200))
        self.mFrame.createStatic("Name", 0, 0)
        self.mFrame.createButton("Check",30, 0, 10, self.OnClick)
        self.mName = self.mFrame.createText(6, 0, 20)
        self.mFrame.createStatic("Age", 0, 1)
        self.mFrame.createButton("Cfg Write",30, 1, 10, self.OnCfgWrite)
        self._Sel = self.mFrame.createCombo(-1, 0, ["COM1","B"])
        #self._Sel.SetSelection(int(config.get("Main","COM")))
        self._Gauge = self.mFrame.createGauge(0, 2, 20)
        self._Gauge.SetValue(20)
        
        item = [
                ["M", self.OnSimple, "S"],
                ["1", self.OnSimple, "2"]
                ]
        
        self.mFrame.createMenu("M",item);
        self.mFrame.createMenu("MS",item);
        self.mFrame.Show()
        
        
        
        return True

    def OnSimple(self, event):
        print "You selected the simple menu item"
        #os.popen("ping 127.0.0.1 -n 10")
        #os.spawnv(os.P_NOWAIT, 'ping', None)
        #pid = Popen(["ping", "127.0.0.1 -n 10"]).pid
        #print subprocess.call(["dir", ""], shell=True)
        self.mFrame.runCmdCbk("ping 127.0.0.1 -n 10", None, self.OnCmdCbk)


    def OnClick(self, event):
        #data = self.mFrame.DoFileDialog()
        #self.mName.SetValue(self.mName.GetValue() + "NAME")
        data = self._Sel.GetSelection()
        self.mName.SetValue(str(data))
        self._Gauge.SetValue(data*100)
        return

    def OnCfgWrite(self, event):
        config = ConfigParser.ConfigParser()

        config.add_section("Main")
        config.set("Main", "COM", str(self._Sel.GetSelection()))
        config.set("Main", "POS", "4")

        config.write(open('cfg.ini', "w"))


    def OnCmdCbk(self, event):
        #self.panel.SetTitle("Click Count: %s" % event.GetClickCount())
        print event.getString(),
        pass
#    def OnIdle(self, event):
#        self._Count = self._Count + 1
#        print self._Count
        #self._Gauge.SetValue(self._Count)
        

if __name__ == '__main__':
    #app = App(redirect=True,filename="mylogfile.txt")
    app = App()
    app.MainLoop()


