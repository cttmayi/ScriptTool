import wx
import Basic.Panel
from Util.Util import dynLoad

#for build
from Basic.Module import module

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
        self.SetScrollRate(20, 20)

    def __onRClickAction(self, event):
        event.Skip()
        pass
    
    def addModule(self, name, x, y):
        moduleFolder = 'Tabs.Modules'
        dyn = dynLoad(moduleFolder+'.'+name,['*'])
        ins = dyn.getClassInstance('moduleFrame', self, name, (x, y))
        return ins
    
    def openTab(self, name, data):
        if (self.frame.tabFrames.has_key(name)):
            tid = self.frame.tabFrames[name][0]
            ins = self.frame.tabFrames[name][1]
            ins.onOpenTab(data)
            self.frame.notebook.SetSelection(tid)
            return True
        return False
    
    def setFramePosition(self, height):
        if self.isCreated:
            self.frame.setFramePosition(height)
        else:
            self.frameHeight = height
        
    def performResume(self, event):
        if self.frameHeight == None:
            self.frameHeight = self.maxHeight + 50
            size = wx.DisplaySize()
            if self.frameHeight < size[1]/2:
                self.frameHeight = size[1]/2
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
    
    def onOpenTab(self, data):
        pass
