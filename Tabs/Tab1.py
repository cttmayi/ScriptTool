
from Basic.TabPanel import tabPanel

from Util.Util import util

class tabFrame(tabPanel):
    tree = None

    def onCreate(self):
        self.tabName = 'DEMO'
        #colors = ["red", "blue", "gray", "yellow", "green"]
        self.SetBackgroundColour("gray")
        
        self.createStatic("Name:", 2, 2)
        
        self.createButton("RunCmdCbk", 8, 2, 15, self.OnClickRunCmdCbk)
        self.createButton("InputWait", 8, -1, 15, self.OnClickInputWait)
        self.createButton("SendMessage", 8, -1, 15, self.onClickSendMessage)
        self.createButton("Dialog", 8, -1, 15, self.onClickDialog)
        self.createButton("Log", 8, -1, 15, self.onClickLog)
        self.createButton('Tree',8, -1, 15, self.onClickTree)
        self.createButton('DirDialog',8, -1, 15, self.onFileDialog)
        
        self.tree = self.createTree(-1 , 2, 30, 10)
        root = self.tree.addItem(None, 'dataA', 'AB', 'C')
        self.item = self.tree.addItem(root, "dataB")
        
        print self.tree.getItemData(root)
        
        datas = ["1", '2', '3']
        datas_data = ["A","B", "C"]
        self.tree.addItems(self.item, datas, datas_data)
        
        #self.tree.deleteItem()
        
        #self.tree.setSelAction(self.OnSelChanged)
        self.tree.setExpandAction(self.OnExpand)
        self.tree.setRClickAction(self.onTreeRightClick)
        #self.tree.expandItem(root)
        #self.tree.expandTreeItem(item)
        
        #self.tree.deleteTreeItem(item)
        
        table = self.createTable(-1, 2, 60, 10, ['A','B','C'])
        table.setColWidth(0, 30)
        table.setColWidth(1, 30)
        table.setColWidth(2, 50)
        table.insertItem(2, ['1','1'])
        table.insertItem(2, ['2','2'])
        table.insertItem(2, ['3','3'])
        table.insertItem(2, ['S','S'])
        table.insertItem(2, ['5','5'])
        table.insertItem(2, ['6','6'])
        table.setItem(2, 0, 'A')
        
        #table.deleteItem()
        table.setRClickAction(self.onTreeRightClick)
        self.table = table

        
        button = self.createButton("A", -1, 2, 5, self.OnClick, 1)
        button.setEnable(False)
        button.setEnable(True)
        self.text = self.createEdit(-1, 2, 50, 10)
        
        #self.createGauge(-1, 2, 10)
        
        self.sel = self.createCombo(-1, 2, ["COM1","COM2"])
        self.sel.setSel(1)
        
        self.bmp = self.createBitmap(5,12,20,10)
        self.bmp.setBitmap('d:\\1.jpg')
        
        self.popupA = self.createPopupMenu()
        self.popupA.addItem("A", self.OnClick)
        self.popupA.addItem("B", self.OnClick)
        
        
        #self.popupB = self.createPopupMenu()
        #self.popupB.addItem("A", self.OnClick)
        #self.popupB.addItem("B", self.OnClick)
        #self.popupB.addItem("C", self.OnClick)
        
        #self.tree.setRClickAction(self.OnRClickB)
        
        self.createCheckbox(-1, 12, 20, ['A', 'B']).setAction(self.onCheckbox)
        
        self.createRadiobox(-1, 12, 'Sel', ['ABCD','B']).setAction(self.onRadio)
        
        self.createEdit(-1, 12, 20, 2).setChangeAction(self.onCheckbox)
        ce = self.createComboEdit(-1, 12, 20, ['A', 'B'])
        ce.deleteItem(0)
        ce.addItem('C')
        
        t = self.createTab(-1, 12, 20, 10)
        #t.addEdit('Edit')
        #t.addTree('Tree')
        m = t.addTable('Table', ['A','B','C'])
        m.setColWidth(0, 30)
        m.setColWidth(1, 30)
        m.insertItem(0, ['1','1'])
        
        
        print self.getCfg('A')
        self.setCfg('A', 'b')
        
        
        #ce = self.createComboEdit(300, 10, 20, ['A', 'B'])
        
        self.setFramePosition(400)
        
        
        return

    def onResume(self):
        print 'TAB1 set Focus'
        
    def onPause(self):
        print 'TAB1 kill Focus'

    def onRadio(self):
        print self
        print 'Radio'

    def onCheckbox(self, cid):
        print cid

    def onDoList(self):
        print 'list'
        print self.table.getItem(self.table.getSel(), 0)

    def OnSelChanged(self):
        text = self.tree.getSelText()
        data = self.tree.getSelData()
        print text, data
        self.printWLine(text)
    
    def OnExpand(self, item):
        self.tree.addItem(item, "A")
        
    def onTreeRightClick(self):
        print 'b'
        self.popupA.show()
        print 'a'
        pass
    
    def onPass(self, event):
        pass
    
    def OnClick(self, bid):
        #self.ClrprintW()
        #self.setOutputColor('yellow');
        self.printW('123456\n123456\n123456\n123456\n')
        #self.setOutputColor('black');
        self.printW("ABCDEF\n")
        #self.setOutputStringColor('123')
        #self.bmp.setBitmap('d:\\1.jpg', 300, 300)
        self.printW(self.text.getText())
        
        #self.runCmdCbk("ping 127.0.0.1 -n 10", None, self.OnCmdCbk, 2000)
        #self.runCmdCbk("cmd", None, self.OnCmdCbk, 1000)
        
        print util.lgStEd('A=0\nB=0\n\nCD=0\r', ['A','B',''])
        
        print util.lgAttr('Frames: containing=[0,0][540,960] parent=[0,0][540,960] display=[0,0][540,960]\r\nCont: containing=[0,0][540,960] parent=[0,0][540,960] display=[0,0][540,960]\n', '=', ' ', ':')

        self.frame.setFramePosition(100)


    def OnClickRunCmdCbk(self, bid):
        self.thread = self.frame.runCmdCbk("cmd", None, self.OnCmdCbk)
        #print util.runWait('ping 127.0.0.1 -n 10', 0)
        #a = util.dir2tree('D:\\bak')
        #a.show()
        #self.tree.setTree(self.tree.root, a)
        pass
        
    def OnClickInputWait(self, bid):
        #self.thread.input('dir')
        
        print self.thread.inputWait('dir', None, 5000, 1000, self.printW)
        
        #r = util.lgMap('com.android.map', '.')

        #for i in range(20):
        #    self.Log(['message'])
        
        
        #r.show()
        
        #print self.frame.doFileDialog('C:')
        
        pass

    def onClickSendMessage(self):
        self.frame.sendMessage(self.doMessage, 0)
        
    def doMessage(self, data):
        print data
        pass
    
    def onClickLog(self):
        
        #self.frame.setLogFormat([['R', 10], ['RR', 20]])
        
        for i in range(1000):
            self.frame.log(['A', 'B'], 'red')
            self.frame.log(['A', 'C'])
            self.frame.log(['A', 'C'])
            self.frame.log(['A', 'C'])
            self.frame.log(['A', 'C'])
            self.frame.log(['A', 'C'])
            self.frame.log(['D', 'C'])
        
        pass
    
    def onClickTree(self):
        a = util.dir2tree('D:\\test')
        a.show()
        self.tree.setTree(self.tree.root, a, True)
    
    def onFileDialog(self):
        print self.frame.doFileDialog('C:\\', '*')
    
    def onClickDialog(self):
        dlg = self.createDialog('Title', 20)
        edit = dlg.createEdit('Name:')
        dlg.createEdit('Age:')
        dlg.createCombo('age', ['30', '31'])
        dlg.createOkCancel()
        
        if dlg.show() == True:
            print edit.getText()
        dlg.Destroy()
        pass

    def OnCmdCbk(self, string):
        #self.panel.SetTitle("Click Count: %s" % event.GetClickCount())
        print string,
        #thread = event.getThread()
        #thread.stop()
        pass
    
    def OnRClickA(self, event):
        self.popupA.show()
        #event.Skip()
        
        
    def OnRClickB(self, event):
        self.popupB.show() 
        event.Skip()
