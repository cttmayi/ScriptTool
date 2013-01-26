
import Basic.Panel
 
########################################################################
class tabPanel(Basic.Panel.panel):
    #----------------------------------------------------------------------
    
    
    
    def __init__(self, parent, frame):
        Basic.Panel.panel.__init__(self, parent, frame)
        self.tabName = None
        self.frameHeight = None
        self.onCreate()
        
        print self.maxWidth, self.maxHeight
        print self.MaxWidth, self.MaxHeight
        
        
        self.SetVirtualSize((self.maxWidth, self.maxHeight))
        self.SetScrollRate(20,20)
        
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
        print 'onDestroy'
        pass
    
