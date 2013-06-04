

import wx
import os
from Util.Util import util
from Util.Util import dynLoad
from Util.Util import cmdThread
import ConfigParser

from Util.Misc import misc
from Util.Global import globals

# for build
from Basic.TabPanel import tabPanel
from Basic.Menu import menu

from Basic.Dialog import dialog

class customerEvent(wx.PyCommandEvent):
    def __init__(self, pid, eventType, data):
        self.eventType = eventType
        wx.PyCommandEvent.__init__(self, self.eventType, pid)
        self.data = data




class mainFrame(wx.Frame):
    
    panel = None
    outPanel = None
    menuBar = None
    statusBar = None
    
    def __init__(self, _name, _pos=(0,0), _size = None):
        g = globals.getInstance()
        
        self.cfg_name = g.configFileName #'cfg.ini'
        
        self.TEXT_W = g.uiTextWidth
        
        if (_size == None):
            size = wx.DisplaySize()
            _size = (size[0], size[1] - 50)
        
        #width = _size[0]
        height = _size[1] - 100
        
        wx.Frame.__init__(self, None, -1, _name, pos=_pos, size=_size)

        self.timers = {}

        if (not os.path.isfile(self.cfg_name)):
            tmpFile = open(self.cfg_name, "w")
            tmpFile.close()
            pass

        tmpDir = 'Temp'
        if not os.path.isdir(tmpDir):
            os.makedirs(tmpDir)

        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open(self.cfg_name, 'r'))

        self.misc = misc.getInstance()
        self.misc.setFrame(self)


        self.menuBar = wx.MenuBar()
        self.SetMenuBar(self.menuBar)

        Mode = 1

        if (Mode == 0):
            self.panel = wx.Panel(self, -1)
        elif (Mode == 1):
            splitter = wx.SplitterWindow(self, style = wx.SP_3D| wx.SP_LIVE_UPDATE)
            TopPanel = wx.Panel(splitter)
            BottomPanel = wx.Panel(splitter)
            splitter.SplitHorizontally(TopPanel, BottomPanel)
            PanelSizer=wx.BoxSizer(wx.VERTICAL)
            PanelSizer.Add(splitter, 1, wx.EXPAND | wx.ALL)
            self.SetSizer(PanelSizer)
            
            splitter.SetSashPosition(height - 200)
            
            self.panel = TopPanel
            self.outPanel = BottomPanel
        elif (Mode == 2):
            TBsplitter = wx.SplitterWindow(self, style = wx.SP_3D| wx.SP_LIVE_UPDATE)
            topPanel = wx.Panel(TBsplitter)
            bottomPanel = wx.Panel(TBsplitter)
            TLRsplitter = wx.SplitterWindow(topPanel, style = wx.SP_3D| wx.SP_LIVE_UPDATE)
            leftPanel = wx.Panel(TLRsplitter)
            rightPanel = wx.Panel(TLRsplitter)
            topPanel.SetBackgroundColour('YELLOW GREEN')
            bottomPanel.SetBackgroundColour('SLATE BLUE')
            leftPanel.SetBackgroundColour('SEA GREEN')
            rightPanel.SetBackgroundColour('STEEL BLUE')
            
            TLRsplitter.SplitVertically(leftPanel, rightPanel) 
            PanelSizer = wx.BoxSizer(wx.VERTICAL)
            PanelSizer.Add(TLRsplitter, 1, wx.EXPAND | wx.ALL)
            topPanel.SetSizer(PanelSizer)
            
            TBsplitter.SplitHorizontally(topPanel, bottomPanel)
            PanelSizer = wx.BoxSizer(wx.VERTICAL)
            PanelSizer.Add(TBsplitter, 1, wx.EXPAND | wx.ALL)
            self.SetSizer(PanelSizer)
            self.panel = leftPanel
            self.outPanel = BottomPanel 

        self.Vsplitter = splitter

#output
        notebookLog = wx.Notebook(self.outPanel)
        
        pt = wx.Panel(notebookLog)
        #ot = wx.TextCtrl(self.outPanel, -1, "Welcome!\n", style=wx.TE_MULTILINE|wx.TE_RICH2)
        ot = wx.TextCtrl(pt, -1, "Welcome!\n", style = wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        wx.Log.SetActiveTarget(wx.LogTextCtrl(ot))
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(ot, 1, wx.ALL|wx.EXPAND, 5)
        pt.SetSizer(sizer)
        notebookLog.AddPage(pt, 'Message')
        self.output = ot
        
#Log
        pt = wx.Panel(notebookLog)
        ot = wx.ListCtrl(pt, style = wx.LC_REPORT )
        columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
        for i in range(len(columns)):
            ot.InsertColumn(i, columns[i])
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(ot, 1, wx.ALL|wx.EXPAND, 5)
        pt.SetSizer(sizer)
        notebookLog.AddPage(pt, 'Log')
        self.outList = ot
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebookLog, 1, wx.ALL|wx.EXPAND, 5)
        self.outPanel.SetSizer(sizer)
        self.maxLogNumber = 1000
        self.clearLogNumber = 100
        self.curLogNumber = 0
        
#status
        self.statusBar = self.CreateStatusBar()


#menu
        menuFolder = 'Menus'
        files = util.listfile(menuFolder)
        for filename in files:
            name = util.dir2module(filename)
            if (name != None):
                try:
                    dyn = dynLoad(menuFolder + '.' + name, ['*'])
                    ins = dyn.getClassInstance('menuFrame', self)
                    if ins.menuName == None:
                        ins.menuName = name
                    self.menuBar.Append(ins, ins.menuName)
                except:
                    print 'Menu(' + name + ') error.'

#tab
        self.tabFrames = {}
        tabId = 0
        notebook = wx.Notebook(self.panel)
        tabFolder = 'Tabs'
        files = util.listfile(tabFolder)
        
        for filename in files:
            name = util.dir2module(filename)
            if (name != None):
                try:
                    dyn = dynLoad(tabFolder+'.'+name,['*'])
                    ins = dyn.getClassInstance('tabFrame', notebook, self)
                    ins.performCreate()
                    if ins.tabName == None:
                        ins.tabName = name
                    notebook.AddPage(ins, ins.tabName)
                    self.tabFrames[ins.tabName] = [ tabId, ins ]
                    tabId = tabId + 1
                except Exception as e:
                    ins.Destroy()
                    print 'Tab(' + name + ') error.'
                    print e
        
        notebook.GetPage(0).performResume(None)
        notebook.SetSelection(0)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.panel.SetSizer(sizer)
        notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.onNotebookPageChange, notebook)
        
        self.notebook = notebook
        
        self.Bind(wx.EVT_CLOSE, self.onCloseWindow)  
        
        self.EVENT_CUSTOMER = wx.NewEventType()
        EVT_CUSTOMER = wx.PyEventBinder(self.EVENT_CUSTOMER, 1)
        self.Bind(EVT_CUSTOMER, self.onCustomerEvent, self.panel)
        
        
        self.panel.Layout()
        self.panel.Refresh()
        self.Layout()
        self.Refresh()
        self.Show()
    

    def onNotebookPageChange(self, event):
        #print event.Selection
        #print event.OldSelection
        
        new_page = self.notebook.GetPage(event.Selection)

        if event.OldSelection > -1:
            old_page = self.notebook.GetPage(event.OldSelection)
        else:
            old_page = new_page
        
        old_page.performPause(event)
        new_page.performResume(event)
        old_page.performStop(event)
        
        event.Skip()
        pass

    def onCloseWindow(self, event):
        sel = self.notebook.GetSelection()
        self.notebook.GetPage(sel).performPause(event)
        self.notebook.GetPage(sel).performStop(event)
        
        count = self.notebook.GetPageCount()
        for pid in range(count):
            self.notebook.GetPage(pid).performDestroy(event)
        
        event.Skip()

    def sendMessage(self, function, data):
        event = customerEvent(self.panel.GetId(), self.EVENT_CUSTOMER, [function, data])
        self.GetEventHandler().AddPendingEvent(event)

    def onCustomerEvent(self, event):
        #print 'onCustomerEvent'
        function = event.data[0]
        data = event.data[1]
        function(data)
        pass

    def setFramePosition(self, height):
        self.Vsplitter.SetSashPosition(height)

    def getFramePosition(self):
        return self.Vsplitter.GetSashPosition()


    def setTabByName(self, name):
        sel = self.tabFrames[name]
        self.notebook.SetSelection(sel)

    def doFileDialog(self, defaultPath = None, filefilter = '*.*'):
        #wildcard = "All files (*.*)|*.*"
        wildcard = "files (" + filefilter + ")|" + filefilter
        path = None
        
        dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", wildcard, wx.OPEN)
        if defaultPath != None :
            dialog.SetPath(defaultPath)
        
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
        dialog.Destroy()
        return path
    
    def doDirDialog(self, defaultPath = None):
        path = None
        dialog = wx.DirDialog(None, "Choose a directory:",
                              style = wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        
        if defaultPath != None :
            dialog.SetPath(defaultPath)
        
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
        dialog.Destroy()
        return path

    def createDialog(self, title, w):
        w = self.TEXT_W * w
        wdt = dialog(self, title, w)
        return wdt


    def runCmdCbk(self, cmd, fcbk = None, lcbk = None):
        EVT_CMD_FINISH = None
        EVT_CMD_LINE = None
        
        if (lcbk):
            EVT_CMD_LINE = wx.NewEventType()
            EVT_CMD_BINDER_LINE = wx.PyEventBinder(EVT_CMD_LINE, 1)
            self.panel.Bind(EVT_CMD_BINDER_LINE, self.__onRunCmd, self.panel)
        
        if (fcbk):
            EVT_CMD_FINISH = wx.NewEventType()
            EVT_CMD_BINDER_FINISH = wx.PyEventBinder(EVT_CMD_FINISH, 1)
            self.panel.Bind(EVT_CMD_BINDER_FINISH, self.__onRunCmd, self.panel) 
        
        thread = cmdThread(cmd, self.panel, EVT_CMD_FINISH, fcbk, EVT_CMD_LINE, lcbk)
        thread.start()
        #thread.join()
        return thread
        
    def __onRunCmd(self, event):
        edata = event.getData()
        fun = edata[0]
        if len(edata) == 2:
            data = event.getData()[1]
            fun(data)
        else:
            fun()

        
    def printW(self, text):
        self.output.AppendText(text)
        self.output.ScrollLines(1)
        
    def printL(self, text):
        self.output.AppendText('' + text + '\n')
        #self.output.ScrollLines(1)
        #wx.LogMessage(text)

    def clrPrint(self):
        self.output.Clear()
    
    def printStatus(self, text):
        self.statusBar.SetStatusText(text)

    def log(self, datas, color = None, scroll = True):
        out = self.outList

        if self.curLogNumber > self.maxLogNumber:
            for i in range(self.clearLogNumber):
                out.DeleteItem(0)
            self.curLogNumber = self.curLogNumber - self.clearLogNumber

        index = out.InsertStringItem(self.maxLogNumber, datas[0])
        self.curLogNumber = self.curLogNumber + 1
        for i in range(1, len(datas)):
            out.SetStringItem(index, i, datas[i])
        
        if color != None:
            item = self.outList.GetItem(index)
            item.SetTextColour(color)
            self.outList.SetItem(item)  
        
        if (scroll == True):
            out.ScrollLines(1)
        
    def setLogFormat(self, formats = [['A', 10]]):
        out = self.outList
        out.DeleteAllItems()
        out.DeleteAllColumns()
        for i in range(len(formats)):
            out.InsertColumn(i, formats[i][0])
            out.SetColumnWidth(i, formats[i][1] * self.TEXT_W)
        pass

    def setTimer(self, func, time):
        if self.timers.has_key(func):
            timer = self.timers[func]
            if time != 0:
                timer.Stop()
                #self.Bind(wx.EVT_TIMER, func, timer)
                timer.Start(time)
            else:
                timer.Stop()            
        else:
            if time != 0:
                timer = wx.Timer(self)
                self.timers[func] = timer
                self.Bind(wx.EVT_TIMER, func, timer)
                timer.Start(time)
    
    

'''
    def setOutputStringColor(self, text, color = wx.RED, pos = -1):
        strs = self.output.GetValue()
        if (pos == -1):
            pos = 0
        else:
            pos = self.output.GetLastPosition() - pos
        while(True):
            s = strs.find(text, pos)
            if (s == -1):
                break
            pos = s + 1
            e = len(text) + s
            self.output.SetStyle(s, e, wx.TextAttr(color))
   
    def setOutputColor(self, fcolor, bcolor = wx.WHITE):
        self.output.SetDefaultStyle(wx.TextAttr(fcolor, bcolor))
'''
   

   

class mainApp(wx.App):
    mFrame = None
        
    def OnInit(self):
        return True

