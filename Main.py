
from MainFrame import *

class App(MainApp):
    def OnInit(self):
        self._Frame = MainFrame((240,300))
        self._Frame.CreateStatic("Name", (10,50))
        self._Name = self._Frame.CreateText((50,50))
        self._Frame.CreateStatic("Age", (10,80))
        self._Frame.CreateButton("Check",(160,50),self.OnClick)
        self._Sel = self._Frame.CreateCombo((10,150), ["A","B"])
        self._Sel.SetSelection(1)
        self._Gauge = self._Frame.CreateGauge((10,200), (250, 25), 50)
        self._Gauge.SetValue(20)
        self._Frame.Show()
        return True

    def OnClick(self, event):
        path = self._Frame.DoFileDialog()
        #self._Name.SetValue(self._Name.GetValue() + "NAME")
        self._Name.SetValue(path)
        return


#    def OnIdle(self, event):
#        self._Count = self._Count + 1
#        print self._Count
        #self._Gauge.SetValue(self._Count)
        

if __name__ == '__main__':
    app = App()
    app.MainLoop()
