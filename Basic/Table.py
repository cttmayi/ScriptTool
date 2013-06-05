import wx

class table(wx.ListCtrl):
    
    
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
    
    
    def getSel(self):
        return self.GetFocusedItem()
    
    def setSel(self, row):
        self.Focus(self, row)
    
    def getItemText(self, row, col):
        item = self.GetItem(row, col)
        return item.GetText()

    def getItemCount(self):
        return self.GetItemCount()

    
    def insertItem(self, row, datas):
        index = self.InsertStringItem(row, datas[0])
        for i in range(1, len(datas)):
            self.SetStringItem(index, i, datas[i])
    
    def setItemText(self, row, col, data):
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

    def setColWidth(self, col, width = None):
        totalWidth = self.GetSize()[0]
        
        if (width != None):
            width = totalWidth * width / 100
            self.SetColumnWidth(col, width)
        else:
            self.SetColumnWidth(col, wx.LIST_AUTOSIZE)
            
    def setRClickAction(self, action):
        self.rclick_cbk = action
        self.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.__onRClickAction)
            
    def __onRClickAction(self, event):
        if self.rclick_cbk != None:
            self.rclick_cbk()
        event.Skip()            
    