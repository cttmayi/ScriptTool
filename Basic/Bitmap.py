
import wx


class bitmap(wx.StaticBitmap):
    def __init__(self, parent, pos, size):
        self.widget = None
        self.width = size[0]
        self.height = size[1]
        
        self.realX = pos[0]
        self.realY = pos[1]
        self.parent = parent
        
        self.bmpH = 0
        self.bmpW = 0
    
    def setBitmap(self, path, w = 0, h = 0):
        if self.widget != None:
            self.widget.Destroy()
            self.widget = None
            
        if path == None:
            return True
        
        self.widget = wx.StaticBitmap(self.parent, -1, pos = (self.realX, self.realY))
        
        
        ext = path.split('.')[-1]
        img = None
        
        if (w == 0):
            w = self.width
        if (h == 0):
            h = self.height
        
        if (ext == 'jpg'):
            img = wx.Image(path, wx.BITMAP_TYPE_JPEG)
        if (ext == 'png'):
            img = wx.Image(path, wx.BITMAP_TYPE_PNG)
            
        
        
        if (img == None or img.IsOk() == False):
            return

        hh = img.GetHeight()
        ww = img.GetWidth()
        
        self.bmpW = ww
        self.bmpH = hh
        
        if (w == 0 and h == 0):
            w = ww
            h = hh
        elif (w == 0):
            w = ww * h / hh
        elif (h == 0):
            h = hh * w / ww
        else:
            if (w * hh > h * ww):
                w = ww * h / hh
            else:
                h = hh * w/ ww

        self.realW = w
        self.realH = h

        if (hh != h or ww != w):
            img = img.Scale(w, h, 0.95)

        bmp = img.ConvertToBitmap()
        self.widget.SetBitmap(bmp)
        self.widget.Refresh()
        
    def setLeftClickAction(self, cbk):
        self.widget.Bind(wx.EVT_LEFT_DOWN, self.__onLeftClickAction)
        self.__leftClickCbk = cbk
        #self.parent.setLeftClickAction(self.realX, self.realY, self.realW, self.realH, cbk)
        
    def __onLeftClickAction(self, event):
        x = event.GetX()
        y = event.GetY()
        
        x = x * self.bmpW / self.realW
        y = y * self.bmpH / self.realH
        if self.__leftClickCbk.func_code.co_argcount == 1:
            self.__leftClickCbk()
        else:
            self.__leftClickCbk(x, y)
        
    def getBitmapSize(self):
        return [self.bmpW, self.bmpH]
    
    def destrop(self):
        self.widget.Destroy()
        
        

