import ConfigParser
from MainFrame import *

class App(MainApp):

    def OnInit(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open('cfg.ini'))
        
        self._Frame = MainFrame((540,200))
        self._Frame.CreateStatic("Name", 0, 0)
        self._Frame.CreateButton("Check",30, 0, 10, self.OnClick)
        self._Name = self._Frame.CreateText(6, 0, 20)
        self._Frame.CreateStatic("Age", 0, 1)
        self._Frame.CreateButton("Cfg Write",30, 1, 10, self.OnCfgWrite)
        self._Sel = self._Frame.CreateCombo(-1, 0, ["COM1","B"])
        self._Sel.SetSelection(int(config.get("Main","COM")))
        self._Gauge = self._Frame.CreateGauge(0, 2, 20)
        self._Gauge.SetValue(20)

        self._Frame.Show()
        return True

    def OnClick(self, event):
        #data = self._Frame.DoFileDialog()
        #self._Name.SetValue(self._Name.GetValue() + "NAME")
        data = self._Sel.GetSelection()
        self._Name.SetValue(str(data))
        self._Gauge.SetValue(data*100)
        return

    def OnCfgWrite(self, event):
        config = ConfigParser.ConfigParser()

        config.add_section("Main")
        config.set("Main", "COM", str(self._Sel.GetSelection()))
        config.set("Main", "POS", "4")

        config.write(open('cfg.ini', "w"))

#    def OnIdle(self, event):
#        self._Count = self._Count + 1
#        print self._Count
        #self._Gauge.SetValue(self._Count)
        

if __name__ == '__main__':
    app = App()
    app.MainLoop()


