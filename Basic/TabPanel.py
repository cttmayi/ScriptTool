import wx
import Basic.Panel
from Util.Util import dynLoad
 
########################################################################
class tabPanel(wx.ScrolledWindow, Basic.Panel.panel):
    #----------------------------------------------------------------------
    
    def __init__(self, parent, frame):
        wx.ScrolledWindow.__init__(self, parent = parent, style=wx.SUNKEN_BORDER)
        Basic.Panel.panel.__init__(self, frame)
        self.tabName = None
        self.frameHeight = None
        self.isCreated = False
        self.onCreate()
        self.isCreated = True
        
        self.Bind(wx.EVT_CONTEXT_MENU, self.__onRClickAction)
        
        self.SetVirtualSize((self.maxWidth, self.maxHeight))
        self.SetScrollRate(20,20)

    def __onRClickAction(self, event):
        event.Skip()
        pass
    
    def addModule(self, name, x, y):
        moduleFolder = 'Tabs.Modules'
        dyn = dynLoad(moduleFolder+'.'+name,['*'])
        ins = dyn.getClassInstance('moduleFrame', self, (x, y))
        if ins.moduleName == None:
            ins.moduleName = name
        #notebook.AddPage(ins, ins.tabName)
    
    def setFramePosition(self, height):
        if self.isCreated:
            self.frame.setFramePosition(height)
        else:
            self.frameHeight = height
        
        
    def performResume(self, event):
        if self.frameHeight != None:
            self.frame.setFramePosition(self.frameHeight)
        
        self.onResume()
    
    def performPause(self, event):
        self.frameHeight = self.frame.getFramePosition()
        
        self.onPause()
        
    def performDestroy(self, event):
        self.onDestroy()   
    
    def performStop(self, event):
        self.onStop()
        
    def onCreate(self):
        pass
    
    def onResume(self):
        #print 'onResume'
        pass
    
    def onPause(self):
        #print 'onPause'
        pass
    
    def onStop(self):
        pass
    
    def onDestroy(self):
        #print 'onDestroy'
        pass
    
