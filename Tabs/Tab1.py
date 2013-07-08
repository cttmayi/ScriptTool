
from Basic.TabPanel import tabPanel

from Util.Util import util
from Util.Excel import excel

from Util.Misc import misc

from Function.TraceView import traceView

class tabFrame(tabPanel):
    tree = None

    def onCreate(self):
        self.tabName = 'DEMO'
        #colors = ["red", "blue", "gray", "yellow", "green"]
        self.SetBackgroundColour("gray")
        
        self.createStatic("Name:", 1, 1)
        self.createStatic("Name:", 2, 2)
        
        self.createButton("RunCmdCbk", 8, 2, 15, self.OnClickRunCmdCbk)
        self.createButton("InputWait", 8, -1, 15, self.OnClickInputWait)
        self.createButton("SendMessage", 8, -1, 15, self.onClickSendMessage)
        self.createButton("Dialog", 8, -1, 15, self.onClickDialog)
        self.createButton('OpenFile', 8, -1, 15, self.onOpenFile)
        self.createButton("Log", 8, -1, 15, self.onClickLog)
        self.createButton('Tree',8, -1, 15, self.onClickTree)
        self.createButton('DirDialog',8, -1, 15, self.onFileDialog)
        self.createButton('WriteExcel',8, -1, 15, self.onWriteExcel)
        self.createButton('util.split',8, -1, 15, self.onUtilSplit)
        self.createButton('timer start',8, -1, 15, self.onTimerStart)
        self.createButton('timer stop',8, -1, 15, self.onTimerStop)
        self.createButton('goto tab2',8, -1, 15, self.onGotoTab2)
        self.createButton('util',8, -1, 15, self.onUtil)
        self.btnSet = self.createButton('Button.reset', 8, -1, 15, self.btnReset)
        self.createButton('trace',8, -1, 15, self.onTraceView)
        
        
        self.tree = self.createTree(-1 , 2, 30, 10)
        root = self.tree.addItem(None, 'dataA', 'AB', 'C')
        self.item = self.tree.addItem(root, "dataB")
        
        print self.tree.getItemData(root)
        
        datas = ["1", '2', '3']
        datas_data = ["A","B", "C"]
        self.tree.addItems(self.item, datas, datas_data)
        
        #self.tree.deleteItem()
        
        #self.tree.setSelAction(self.OnSelChanged)
        self.tree.setExpandAction(self.onExpand)
        #self.tree.setRClickAction(self.onTreeRightClick)
        #self.tree.expandItem(root)
        #self.tree.expandTreeItem(item)
        #self.tree.deleteTreeItem(item)
        
        table = self.createTable(-1, 2, int(self.getDisplayWidth()/2), 10, ['A','B','C'])
        table.setColWidth(0, 30)
        table.setColWidth(1, 30)
        table.setColWidth(2, 50)
        table.insertItem(2, ['1','1'])
        table.insertItem(2, ['2','2'])
        table.insertItem(2, ['3','3'])
        table.insertItem(2, ['S','S'])
        table.insertItem(2, ['5','5'])
        table.insertItem(2, ['6','6'])
        table.setItemText(2, 0, 'A')
        
        #table.deleteItem()
        table.setRClickAction(self.onTreeRightClick)
        self.table = table

        
        button = self.createButton("A", -1, 2, 5, self.OnClick, 1)
        button.setEnable(False)
        button.setEnable(True)
        self.text = self.createEdit(-1, 2, 50, 10)
        self.text.setEnterAction(self.onEditEnter)
        
        #self.createGauge(-1, 2, 10)
        
        self.sel = self.createCombo(-1, 2, ["COM1","COM2"])
        self.sel.setSel(1)
        
        self.bmp = self.createBitmap(5,18,20,10)
        self.bmp.setBitmap('d:\\1.jpg')
        self.bmp.setLeftClickAction(self.onBitmapCbk)
        
        self.popupA = self.createPopupMenu('P')
        self.popupA.addItem("A", self.onPopupA_A)
        self.popupA.addItem("B", self.onPopupA_B, 'B')
        
        self.tree.setRClickPopup(self.popupA, 'expand')
        
        
        #self.popupB = self.createPopupMenu()
        #self.popupB.addItem("A", self.OnClick)
        #self.popupB.addItem("B", self.OnClick)
        #self.popupB.addItem("C", self.OnClick)
        
        #self.tree.setRClickAction(self.OnRClickB)
        
        self.cbok = self.createCheckbox(-1, 12, 20, ['A', 'B','C', 'D'], 4)
        self.cbok.setAction(self.onCheckbox)
        self.cbok.setSel(True, 0)
        self.cbok.setSel(True, 1)
        self.cbok.setSel(True, 2)
        self.cbok.setSel(True, 3)
        
        self.createRadiobox(-1, 12, 'Sel', ['ABCD','B']).setAction(self.onRadio)
        
        self.createEdit(-1, 12, 20, 2).setChangeAction(self.onCheckbox)
        ce = self.createComboEdit(-1, 12, 20, ['A', 'B'])
        ce.deleteItem(0)
        ce.addItem('C')
        
        t = self.createTab(-1, 12, 20, 10)
        #t.addEdit('Edit')
        #t.addTree('Tree')
        m = t.addTable('Table', ['A','B','C'])
        m.setColWidth(0, 80)
        m.setColWidth(1, 20)
        m.insertItem(0, ['1','1'])
        m = t.addTable('Table', ['A','B'])
        t.setSel(1)
        
        
        print self.getCfg('A')
        self.setCfg('A', 'b')
        
        
        #ce = self.createComboEdit(300, 10, 20, ['A', 'B'])
        
        #self.setFramePosition(400)
        
        
        minst = misc.getInstance()
        if minst.makeInstallTool('Make'):
            print 'pass'
        
        return

    def onResume(self):
        print 'TAB1 set Focus'
        
    def onPause(self):
        print 'TAB1 kill Focus'

    def onRadio(self):
        print 'Radio'

    def onCheckbox(self, cid):
        print self.cbok.getSel(cid)
        print cid

    def onDoList(self):
        print 'list'
        print self.table.getItem(self.table.getSel(), 0)


    def onEditEnter(self):
        print 'enter'
        pass


    def OnSelChanged(self):
        text = self.tree.getSelText()
        data = self.tree.getSelData()
        print text, data
        self.printWLine(text)
    
    def onExpand(self, item):
        t = self.tree.addItem(item, "A")
        self.tree.setItemAttr(t, 'expand')
        
    def onTreeRightClick(self):
        self.popupA.show([0])
        pass
    
    def onPass(self, event):
        pass
    
    def onBitmapCbk(self, x, y):
        print 'bitmap', x, y
    
    
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
        print self.frame.doFileDialog('C:\\', '*.jpg|*.mp3')
    
    def onWriteExcel(self):
        efile = excel.open('file.xls')
        sytleR = excel.createSytle('red', True)
        sytleY = excel.createSytle('yellow', True)
        for i in range(10000):
            excel.write(efile, 'sheet', ['NAME', 'DATE'], [sytleR, sytleY])
        excel.setColWidth(efile, 'sheet', [4, 4, 4, 4])
        
        excel.close(efile)
        
        util.run('file.xls')
        print 'success'
    
    def onUtilSplit(self):
        print util.split('ABCDEF', ['B'])
        print util.split('ABCDEF', ['A'])
        print util.split('ABCDEF', ['A', 'B'])
        print util.split('ABCDEF', ['A', 'F'])
        print util.split('ABCDEF', ['CD', 'F'])
        print util.split('ABCDEFGHIJKL', ['A','CD', 'F', 'IJK'])

    def onTraceView(self):
        filters = [
                ['android.view.InputEventConsistencyVerifier.onTouchEvent', 'onTouchEvent', 'r'],
                ['android.os.MessageQueue.nativePollOnce', 'AP', 'r'],
                ['android.os.Handler.dispatchMessage', 'AP', 'y'],
                ['android.view.ViewRootImpl.finishInputEvent', 'AP2', 'y'],
                ['android.view.MotionEvent.recycle', 'AP2', 'r'],
                ]
        
        path = self.frame.doFileDialog('C:\\', '*.trace')
        if path != None:
            v = traceView(path)
            v.showView(filters)        

    def onClickDialog(self):
        dlg = self.createDialog('Title', 20)
        edit = dlg.createEdit('Name:')
        dlg.createEdit('Age:')
        dlg.createCombo('age', ['30', '31'])
        dlg.createOkCancel()
        
        if dlg.show() == True:
            print edit.getText()
        dlg.destroy()
        pass

    def onOpenFile(self):
        inst = misc.getInstance()
        inst.openFile('D:\\1.jpg', 'jpg')

    def OnCmdCbk(self, string):
        #self.panel.SetTitle("Click Count: %s" % event.GetClickCount())
        print string,
        #thread = event.getThread()
        #thread.stop()
        pass
    
    def OnRClickA(self, event):
        self.popupA.show()
        #event.Skip()
        
    def onPopupA_A(self):
        item = self.tree.getSel()
        self.tree.setItemText(item, 'A')
        print 'A'
        
    def onPopupA_B(self, a, b):
        print 'onPopupA_B'
        print a, b
    
        
    def OnRClickB(self, event):
        self.popupB.show() 
        
    def onTimerStart(self):
        self.frame.setTimer(self.onTimer, 1000)
        pass
    
    def onTimerStop(self):
        self.frame.setTimer(self.onTimer, 0)
        pass
    
    def onGotoTab2(self):
        self.openTab('Tab2', 'todo')
    
    def onUtil(self):
        print util.lgStEd('A=0\nB=0\n\nCD=0\r', ['A','B',''])
        print util.lgAttr('Frames: containing=[0,0][540,960] parent=[0,0][540,960] display=[0,0][540,960]\r\nCont: containing=[0,0][540,960] parent=[0,0][540,960] display=[0,0][540,960]\n', '=', ' ', ':')        
        r = util.lgMap(['com.android.map.a', 'com.android.map'], '.')
        r.show()
        
        pass
    
    def btnReset(self):
        self.btnSet.reset('Set')
        self.sel.reset(['A','B'])
    
    def onTimer(self, e):
        self.frame.printL('onTimer')
        
        
        
    
