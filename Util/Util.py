import os
import signal
import subprocess
import threading
import wx
import tempfile
import time
import StringIO
import thread


class util():
	@staticmethod
	def run(cmd):
		subprocess.Popen(cmd ,shell=True)

	@staticmethod
	def runPara(cmd, para, shell = True):
		if cmd.find(' ') > 0:
			cmd = '"' + cmd + '"'
		util.run(cmd + ' ' + para)
	
	
	@staticmethod
	def runWait(cmd, timeout = 0):
		#subprocess.call(cmd.split(' '), shell=True)
		outFile =  tempfile.SpooledTemporaryFile() 

		proc = subprocess.Popen(cmd, stdout=outFile, stderr=outFile, universal_newlines=False, shell=True)
		wait_remaining_sec = timeout
	

		while proc.poll() is None and (timeout == 0 or wait_remaining_sec > 0):
			time.sleep(0.05)
			wait_remaining_sec -= 50
			#print wait_remaining_sec
		if wait_remaining_sec <= 0 and timeout != 0:
			util.stopCmdbyID(proc.pid)

		outFile.seek(0);
		out = outFile.read()
		outFile.close()
		return out

	@staticmethod
	def runWaitOutputString(cmd, timeout = 0):
		#return subprocess.check_output(cmd.split(' '), shell=True)
		return util.runWait(cmd, timeout)
	
	@staticmethod
	def runPipe(cmd):
		return subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False)
	
	@staticmethod
	def stopCmd(popen):
		if (popen.poll() == None):
			popen.terminate()
		
	@staticmethod
	def stopCmdbyID(pid):
		os.kill(pid, signal.SIGINT)
		
	@staticmethod
	def startThread(function, arg):
		thread.start_new_thread(function,(arg))  
		pass
	
	
	@staticmethod
	def listfile(dirname, IsFullName = True, isRecursion = False):
		files = []
		try:
			ls=os.listdir(dirname)
		except:
			print 'access deny'
			return None
		else:
			for l in ls:
				filename = os.path.join(dirname,l)
				if( not os.path.isdir(filename)):
					if IsFullName == True:
						files.append(filename)
					else:
						files.append(l)
				else:
					if isRecursion:
						rec = util.listfile(filename, IsFullName, isRecursion)
						files = files + rec
					
		return files
	
	@staticmethod
	def listdir(dirname, full = False):
		dirs = []
		try:
			ls=os.listdir(dirname)
		except:
			print 'access deny'
			return None
		else:
			for l in ls:
				filename = os.path.join(dirname,l)
				if(os.path.isdir(filename)):
					if full == True:
						dirs.append(filename)
					else:
						dirs.append(l)
		return dirs

	
	@staticmethod
	def dir2module(_dir):
		filename = _dir.split('\\')[-1]
		[name,ext] = filename.split('.')
		if (ext == 'py' and name[0:2] != '__'):
			return name
		return None
	
	@staticmethod	
	def lgStEd(strs, splits):
		strlist = []
		
		selen = len(splits)
		sid = 0
		
		bufs = StringIO.StringIO(strs)

		sps = splits[sid]
		if (isinstance(sps, list)):
			sp = sps[0]
			spn = sps[1]
		else:
			sp = sps
			spn = ''
		splen = len(sp)
		spnlen = len(spn)
		
		strlist.append('')
		for buf in bufs.readlines():
			if splen != 0 and buf[0:splen] == sp and (spnlen == 0 or buf[0:spnlen] != spn):
				sid = sid + 1
				if sid == selen:
					break
				strlist.append('')
				
				sps = splits[sid]
				if (isinstance(sps, list)):
					sp = sps[0]
					spn = sps[1]
				else:
					sp = sps
					spn = ''
				splen = len(sp)
				spnlen = len(spn)

			strlist[sid] = strlist[sid] + buf
		return strlist
	
	@staticmethod
	def lgAttr(strs, sp2, sp1 = None, spTitle = None):
		attrMap = {}
		
		if not (isinstance(strs, list)):
			strs = strs.split('\n')
		
		strTitle = ''
		
		for strline in strs:
			strline = strline.strip()
			if spTitle != None:
				strTitles = strline.split(spTitle)
				if len(strTitles) == 2:
					strTitle = strTitles[0] + '.'
					strline = strTitles[1]
			
			strline = strline.strip()
			if sp1 != None:
				strsp1 = strline.split(sp1)
			else:
				strsp1 = []
				strsp1.append(strline)
			print strsp1
			for strpart in strsp1:
				strsp2 = strpart.split(sp2)
				if (len(strsp2) == 2):
					attrMap[strTitle + strsp2[0]] = strsp2[1]
		return attrMap

	@staticmethod
	def lgMap(strs, sp = '.', prePackage = '', preClass = ''):
		root = tree('root')
		if not (isinstance(strs, list)):
			strs = strs.split('\n')
			
		for strline in strs:
			strps = strline.split(sp)
			end = strps[-1]
			cont = root
			for strp in strps:
				if (strp != ''):
					if (strp != end):
						cont = cont.add(prePackage + strp, None, 'package')
					else:
						cont = cont.add(preClass + strp, strline, 'class')
		return root
	
	@staticmethod
	def dir2tree(dirname):
		name = dirname.split('\\')[-1]
		r = tree(name, dirname, 'dir')
		try:
			ls=os.listdir(dirname)
		except:
			print 'access deny'
		else:
			for simp in ls:
				full = os.path.join(dirname, simp)
				
				if(os.path.isdir(full)):
					c = util.dir2tree(full)
					r.addtree(c)
				else:
					r.add(simp, full, 'file')
		return r
				
	@staticmethod
	def split(strs, sps):
		ret = []
		i = 0
		st = 0
		#for s in range(len(strs)):
		s = 0
		while(s < len(strs)):
			if strs[s: s+len(sps[i])] == sps[i]:
				ret.append(strs[st:s])
				s = s + len(sps[i]) - 1
				st = s + 1

				i = i + 1
				if i == len(sps):
					ret.append(strs[st:len(strs)])
					return ret
			s = s + 1
		return ret
	
	@staticmethod
	def joinFileSubName(fileName, subName):
		'''
		input: Temp\Log.log ams
		output: Temp\Log_ams.log
		'''
		
		Filedir = os.path.dirname(fileName)
		p = os.path.basename(fileName)
		[f, e] = os.path.splitext(p)
		filePath = os.path.join(Filedir, f  + '_' + subName + e)
		return filePath
	
	@staticmethod
	def grep(inFile, names):
		ret = []
		fp = open(inFile, 'r')
		n = 0
		for line in fp.readlines():
			n = n + 1
			for name in names:
				if line.find(name) > -1:
					ret.append([name, inFile, n, line])
					
		if len(ret) == 0:
			ret = None
		return ret


class dynLoad():
	def __init__(self,package,imp_list):
		self.package=package
		self.imp=imp_list
		self.obj = self.getObject()

	def getObject(self):
		return __import__(self.package, globals(), locals(),self.imp, -1)
	def getClassInstance(self, classstr, *args):
		return getattr(self.obj,classstr)(*args)   
	def execfunc(self,method,*args):
		return getattr(self.obj, method)(*args)
	def execMethod(self,instance,method,*args):
		return getattr(instance, method)(*args)
	
	
class cmdEvent(wx.PyCommandEvent):
	def __init__(self, evtType, eid):
		wx.PyCommandEvent.__init__(self, evtType, eid)
		self.data = None
#		self.cbk = None

	def getData(self):
		return self.data

	def setData(self, data):
		self.data = data

class cmdThread(threading.Thread):
	def __init__(self, cmd, panel, evt_finish, fun_finish, evt_line, fun_line, timeout = 0):
		threading.Thread.__init__(self)
		self.event_line = evt_line
		self.fun_line = fun_line
		self.event_finish = evt_finish
		self.fun_finish = fun_finish
		#self.fun_finish_arg = fun_finish.func_code.co_argcount
		self.panel = panel
		self.popen = util.runPipe(cmd)
		self.output_pipe =  self.popen.stdout
		self.input_pipe = self.popen.stdin
		
		self.fgOutData = False
		self.fgWaitStop = False
		self.stringStop = None
		
		if (timeout != 0):
			wx.FutureCall(timeout, self.stop)
	
	def stop(self):
		#print ['stop pid:',self.popen.pid]
		util.stopCmd(self.popen)
		#util.stopCmdbyID(self.popen.pid)

	def input(self, cmd):
		#print 'cmd: ' + cmd
		self.input_pipe.write(cmd +'\n')
		
	def inputWait(self, cmd, strStop = None, timeout_start = 500, timeout_data = 100, cbk = None):
		self.outData = []
		self.fgOutChange = False
		self.fgOutData = True
		self.fgWaitStop = False
		self.stringStop = strStop
		
		wait_remaining_sec = timeout_start
		time_last = time.time()
		list_id = 0
		
		
		
		self.input(cmd)

		while (True):
			self.fgOutChange = False
			time.sleep(0.05)
			
			t = time.time()
			time_step = (t - time_last) * 1000
			time_last = t
			wait_remaining_sec -= time_step
			#print wait_remaining_sec
			
			if (cbk != None):
				while(list_id < len(self.outData)):
					cbk(self.outData[list_id])
					list_id = list_id + 1
			
			if (self.fgOutChange and wait_remaining_sec < timeout_data):
				wait_remaining_sec = timeout_data
				
			if wait_remaining_sec <= 0 or self.fgWaitStop == True:
				break
		
		self.fgOutData = False
		
		return self.outData

	def run(self):
		if (self.event_line):
			while (True):
				string =  self.output_pipe.readline()
				if (string and self.fgOutData):
					self.outData.append(string)
					self.fgOutChange = True
					if self.stringStop != None:
						if (string.find(self.stringStop) >= 0):
							self.fgWaitStop = True
				elif (string):
					evt = cmdEvent(self.event_line, self.panel.GetId())
					evt.setData([self.fun_line, string])
					#evt.setThread(self)
					self.panel.GetEventHandler().AddPendingEvent(evt)
				else:
					break
			if (self.event_finish):
				evt = cmdEvent(self.event_finish, self.panel.GetId())
				evt.setData([self.fun_finish])
				#evt.setThread(self)
				self.panel.GetEventHandler().AddPendingEvent(evt)
		else :
			if (self.event_finish):
				string =  self.output_pipe.read()
				evt = cmdEvent(self.event_finish, self.panel.GetId())
				evt.setData([self.fun_finish, string])
				#evt.setThread(self)
				self.panel.GetEventHandler().AddPendingEvent(evt)
				

class tree:
	
	def __init__(self, name, data = None, attr = None):
		self.name = name
		self.data = data
		self.attr = attr
		self.dict = {}
		
	def add(self, name, data = None, attr = None):
		if not self.dict.has_key(name):
			child = tree(name, data, attr)
			self.dict[name] = child
		return self.dict[name]
	
	def addtree(self, ctree):
		name = ctree.name
		if not self.dict.has_key(name):
			self.dict[name] = ctree
		return self.dict[name]
		
		ctree.name
	
	def delete(self, name):
		if self.dict.has_key(name):
			del self.dict[name]
	
	def getName(self):
		return self.name
	
	def getData(self):
		return self.data
	
	def getDict(self):
		return self.dict
	
	def getList(self):
		dlist = []
		for key in self.dict:
			value = self.dict[key]
			dlist.append(value)
		return dlist
	
	def show(self, offset = '-'):
		print offset, self.name, ' (', self.data, ')'
		for key in self.dict:
			v = self.dict[key]
			v.show(offset+'--')
		
		
	
	
		
	
		
				