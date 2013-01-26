
import wx


class bitmap(wx.StaticBitmap):
    def __init__(self, parent, pos, size):
        wx.StaticBitmap.__init__(self, parent, -1, pos = pos)
        self.width = size[0]
        self.height = size[1]
    
    def setBitmap(self, path, w = 0, h = 0):
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
        
        if (img.IsOk() == False):
            return

        hh = img.GetHeight()
        ww = img.GetWidth()
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

        if (hh != h or ww != w):
            img = img.Scale(w, h, 0.95)

        bmp = img.ConvertToBitmap()
        self.SetBitmap(bmp)
        self.Refresh()
        