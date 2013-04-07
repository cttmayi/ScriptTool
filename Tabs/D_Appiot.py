from Basic.TabPanel import tabPanel
from Util.Excel import excel
from Util.Util import util
from Util.Misc import misc

import os

class tabFrame(tabPanel):
	
	def onCreate(self):
		
		self.tabName = 'Appiot'
		
		self.line = 0
		self.createStaticBox('systrace',3, self.line, 80, 2)
		self.line = self.line + 1
		self.createButton("Start", 3, self.line, 10, self.onStartFtrace, 1)
		self.createButton("Stop", -1, self.line, 10, self.onStopFtrace, 1)
		self.createButton("Show", -1, self.line, 10, self.onShowFtrace, 1)
		
		self.line = self.line + 1
		self.createStaticBox('systrace',3, self.line, 80, 3)
		self.line = self.line + 1
		self.createButton("Start", 3, self.line, 10, self.onStartSystrace, 1)
		self.createButton("Show", -1, self.line, 10, self.onShowSystrace, 1)
		self.createButton("Set", -1, self.line, 10, self.onSetSystrace, 1)
		
		self.line = self.line + 1
		self.systraceOption = ['gfx', 'input', 'view', 'wm', 'am', 'sync', 'audio', 'video', 'camera']
		self.systraceCBok = self.createCheckbox(3, self.line, 75, self.systraceOption, len(self.systraceOption))
		
	def onStartFtrace(self):
		self.frame.runCmdCbk("Tool\\ftrace.jb\\M-start.bat", None , self.frame.printL)
		pass
	
	def onStopFtrace(self):
		self.frame.runCmdCbk("Tool\\ftrace.jb\\M-stop.bat", None , self.frame.printL)
		pass

	def onShowFtrace(self):
		util.run("cd Tool\\ftrace.jb && M-show.bat")
		pass

	def onSetSystrace(self):
		option = ''
		for i in range(len(self.systraceOption)):
			if self.systraceCBok.getSel(i):
				option = option + ' ' + self.systraceOption[i]
			print option
		
	
		self.frame.runCmdCbk("Tool\\systrace\\systrace_set.bat" + option, None , self.frame.printL)
		pass
		
	def onStartSystrace(self):
		self.frame.runCmdCbk("Tool\\systrace\\systrace_start.bat 10 gfx,view,wm", None , self.frame.printL)
		pass
	
	def onShowSystrace(self):
		minst = misc.getInstance()
		print os.getcwd()
		minst.openFile(os.getcwd() + '\\Tool\\systrace\\trace.html', 'chrome')	
		pass
		

		