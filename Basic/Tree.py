import wx

class tree(wx.TreeCtrl):
    def __init__(self, panel, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TR_DEFAULT_STYLE):
        wx.TreeCtrl.__init__(self, panel, -1, pos, size, style)
        pass

    def addItem(self, root, name, data = None, attr = None):
        if (root == None):
            _item = self.AddRoot(name)
            self.SetPyData(_item, [data, attr])
            self.root = _item
        else:
            _item = self.AppendItem(root, name)
            self.SetPyData(_item, [data, attr])
        return _item
    
    def addItems(self, root, names, datas = None, attr = None):
        if (isinstance(names, list)):
            items = []
            for i in range(len(names)):
                child = self.AppendItem(root, names[i])
                items.append(child)
                if (datas != None):
                    self.SetPyData(child, [datas[i], attr])
        else:
            child = self.AppendItem(root, names)
            self.SetPyData(child, [datas, attr])
            items = child
        return items
    
    def deleteItem(self, items = None):
        #print type(items)
        if (items == None):
            self.DeleteAllItems()
        elif (isinstance(items, list)):
            for i in range(len(items)):
                self.Delete(items[i])
        else:
            self.Delete(items)
            
    def deleteItemChild(self, item):
        self.DeleteChildren(item)

    def getSel(self):
        item = self.GetSelection()
        return item


    def getSelText(self):
        item = self.GetSelection()
        text = self.GetItemText(item)
        return text
    
    
    def getSelData(self):
        item = self.GetSelection()
        data = self.GetItemPyData(item)[0]
        return data

    def getSelAttr(self):
        item = self.GetSelection()
        attr = self.GetItemPyData(item)[1]
        return attr

    def getItemText(self, item):
        text = self.GetItemText(item)
        return text       

    def setItemText(self, item, text):
        self.SetItemText(item, text)

    def getItemData(self, item):
        data = self.GetItemPyData(item)[0]
        return data
    
    def setItemData(self, item, data):
        attr = self.GetItemPyData(item)[1]
        self.SetItemPyData([data, attr])

    def getItemAttr(self, item):
        attr = self.GetItemPyData(item)[1]
        return attr         

    def setItemAttr(self, item, attr):
        data = self.GetItemPyData(item)[0]
        self.SetItemPyData([data, attr])

    def expandItem(self, item = None):
        if (item == None):
            self.ExpandAll()
        else:
            self.Expand(item)

    def setSelAction(self, action):
        self.sclick_cbk = action
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.onSClickAction)
            
    def onSClickAction(self, event):
        if self.sclick_cbk != None:
            self.sclick_cbk()
        event.Skip()

    def setDClickAction(self, action):
        self.dclick_cbk = action
        self.Bind(wx.EVT_LEFT_DCLICK, self.onDClickAction)
            
    def onDClickAction(self, event):
        if self.dclick_cbk != None:
            self.dclick_cbk()
        event.Skip()
    
    def setExpandAction(self, action):
            self.eclick_cbk = action
            self.Bind(wx.EVT_TREE_ITEM_EXPANDING, self.onEClickAction)
    
    def onEClickAction(self, event):
        if self.eclick_cbk != None:
            item = self.getEventItem(event)
            self.eclick_cbk(item)
        event.Skip()
      
    def setRClickAction(self, action):
        self.rclick_cbk = action
        self.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.__onRClickAction)
            
    def __onRClickAction(self, event):
        item = event.GetItem()
        self.SelectItem(item)
        if self.rclick_cbk != None:
            self.rclick_cbk()
        event.Skip()


    def getEventItem(self, event):
        item = event.GetItem()
        return item
    
    def setTree(self, root, data):
        dicts = data.getDict()
        keys = dicts.keys()
        keys.sort()
        for key in keys:
            v = dicts[key]
            child = self.addItem(root, v.name, v.data, v.attr)
            self.setTree(child, v)
    
    def getTree(self, root):
        pass
        
    
        