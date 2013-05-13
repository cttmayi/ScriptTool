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
		
		
		# apktool
		self.apkFile = None
		self.apkOutputFile = None
		self.line = self.line + 1
		self.createStaticBox('appiot',3, self.line, 80, 2)
		self.line = self.line + 1
		self.createButton("Open", 3, self.line, 10, self.onOpenAppiot)
		self.createButton("Explorer", -1, self.line, 10, self.onOpenExplorer)
		self.createButton("Smali2java", -1, self.line, 10, self.onApkSmali2Java)
		self.createButton("Encoder", -1, self.line, 10, self.onApkEncoder)
		self.createButton("Install", -1, self.line, 10, self.onApkInstall)

		self.line = self.line + 1
		self.createStaticBox('cpu',3, self.line, 80, 2)
		self.line = self.line + 1
		self.createButton("Single core", 3, self.line, 10, self.onSingleCore)
		self.createButton("Dual core", -1, self.line, 10, self.onDualCore)		
		self.createButton("Four Core", -1, self.line, 10, self.onFourCore)
		
		self.line = self.line + 1
		self.createButton("Open Folder", 3, self.line, 10, self.onOpenFolder)
		self.tree = self.createTree(-1, self.line, 30, 10)
		
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
	
#	def sample(self, string):
#		self.frame.printL('-')
#		self.frame.printL(string)
	
	def onOpenAppiot(self):
		apkFile = self.frame.doFileDialog('*.apk')
		
		minst = misc.getInstance()
		if minst.makeInstallTool('apktool') and apkFile != None:
			self.frame.printL('open ' + apkFile)
			apkDir = os.path.dirname(apkFile) + '\\apkOutput'
			#self.frame.runCmdCbk('Tool\\apktool\\apktool.bat d ' + apkFile + ' ' + apkDir, self.sample)
			self.frame.printL(util.runWait('Tool\\apktool\\apktool.bat d ' + apkFile + ' ' + apkDir))
			self.apkFile = apkFile
			
	def onOpenExplorer(self):
		if self.apkFile != None:
			apkDir = os.path.dirname(self.apkFile) + '\\apkOutput'
			util.run('explorer.exe '+ apkDir)
		pass
	
	def onApkSmali2Java(self):
		if self.apkFile != None:
			apkDir = os.path.dirname(self.apkFile) + '\\apkOutput'
			self.frame.printL('smali to java')
			util.runWait('Tool\\apktool\\smali2java2.py ' + apkDir + '\\smali ' + apkDir + '\\java')
			self.frame.printL('finish ...')
			
	
	def onApkEncoder(self):
		if self.apkFile != None:
			apkDir = os.path.dirname(self.apkFile) + '\\apkOutput'
			apkFileName = os.path.basename(self.apkFile)
			apkTempFile = apkDir + '\\dist\\' + apkFileName
			self.apkOutputFile = apkDir + '\\dist\\' + apkFileName[:-4] + '_sign.apk'
			#self.frame.runCmdCbk('Tool\\apktool\\apktool.bat b ' + apkDir, self.frame.printL)
			#self.frame.printL(util.runWait('Tool\\apktool\\apktool.bat b ' + apkDir))
			#self.frame.printL(util.runWait('Tool\\apktool\\sign.bat ' + apkDir + '\\dist\\' + apkFileName + ' ' + self.apkOutputFile))
			#self.frame.runCmdCbk('Tool\\apktool\\encoder.bat ' + apkDir + ' ' + apkTempFile + ' ' + self.apkOutputFile, self.frame.printL)
			self.frame.printL('encoder ' + apkDir)
			self.frame.printL(util.runWait('Tool\\apktool\\encoder.bat ' + apkDir + ' ' + apkTempFile + ' ' + self.apkOutputFile))
	
	def onApkInstall(self):
		if self.apkOutputFile != None and os.path.exists(self.apkOutputFile):
			self.frame.printL('install ' + self.apkOutputFile)
			self.frame.printL(util.runWait('adb install -r ' + self.apkOutputFile))
		pass
		
	def onSingleCore(self):
		pass
	
	def onDualCore(self):
		pass
	
	def onFourCore(self):
		pass		
		
	def onOpenFolder(self):
		path = self.frame.doDirDialog()
		
		if path != None:
			files = util.dir2tree(path)
			root = self.tree.addItem(None, 'root')
			self.tree.setTree(root, files)
		pass
		