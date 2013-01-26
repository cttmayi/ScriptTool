import wx

class table(wx.ListCtrl):
    
    mWidth = 0
    
    def __init__(self, panel, pos = wx.DefaultPosition, size = wx.DefaultSize):
        wx.ListCtrl.__init__(self, panel, -1,
                           pos = pos,
                           size = size,
                           style = wx.LC_REPORT 
                           #| wx.BORDER_SUNKEN
                           #| wx.BORDER_NONE
                           | wx.LC_EDIT_LABELS
                           #| wx.LC_SORT_ASCENDING
                           #| wx.LC_NO_HEADER
                           #| wx.LC_VRULES
                           #| wx.LC_HRULES
                           #| wx.LC_SINGLE_SEL
                           )
        self.mWidth = size[0]
    
    
    def getSel(self):
        return self.GetFocusedItem()
    
    def setSel(self, row):
        self.Focus(self, row)
    
    def getItem(self, row, col):
        item = self.GetItem(row, col)
        return item.GetText()

    
    def insertItem(self, row, datas):
        index = self.InsertStringItem(row, datas[0])
        for i in range(1, len(datas)):
            self.SetStringItem(index, i, datas[i])
    
    def setItem(self, row, col, data):
        self.SetStringItem(row, col, data)
        
    def deleteItem(self, rows = None):
        if (rows == None):
            self.DeleteAllItems()
        else:
            if (isinstance(rows, list)):
                for i in range(len(rows)):
                    self.DeleteItem(rows[i])
            else:
                self.DeleteItem(rows)

    def setColWidth(self, col, width = -1):
        if (width != -1):
            width = self.mWidth * width / 100
            self.SetColumnWidth(col, width)
        else:
            self.SetColumnWidth(col, wx.LIST_AUTOSIZE)
            
    def setRClickAction(self, action):
        self.rclick_cbk = action
        self.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.onRClickAction)
            
    def onRClickAction(self, event):
        if self.rclick_cbk != None:
            self.rclick_cbk()
        event.Skip()            
    