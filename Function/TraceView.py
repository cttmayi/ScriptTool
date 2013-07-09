

import os
import sys
import struct

import matplotlib.pyplot as plt
import pylab
import numpy as np

class methodTrace():
    def __init__(self):
        self.infoLog = {}
        self.infoMethodCall = {}
        self.infoMethodCallEntry = {}
        self.infoThreads = {}
        self.infoMethods = {}
        
        self.fileKey = None
        self.fileData = None
        
        self.timeline = 0
    
    def __subFileName(self, sfile, ext):
        fileDir = os.path.dirname(sfile)
        p = os.path.basename(sfile)
        f= os.path.splitext(p)[0]
        filePath = os.path.join(fileDir, f  + '.' + ext)
        return filePath
        
    def openTraceFile(self, sfile):
        fp = open(sfile, 'rb')
        self.fileKey = self.__subFileName(sfile, 'key')
        self.fileData = self.__subFileName(sfile, 'data')
        
        fpKey = open(self.fileKey, 'wb')
        fpData = open(self.fileData, 'wb')

        keyMode = True
        keyStr = '*end\n'
        n = 0

        while(True):
            datas = fp.read(10000)
            if datas:
                if keyMode == True:
                    for s in datas:
                        if keyMode == True:
                            fpKey.write(s)
                            if s == keyStr[n]:
                                n = n + 1
                                if n == len(keyStr):
                                    keyMode = False
                            else:
                                n = 0
                        else:
                            fpData.write(s)
                else:
                    fpData.write(datas)
            else:
                break

        fp.close()
        fpKey.close()
        fpData.close()

    def parse(self):
        fpKey = open(self.fileKey, 'r')

        fileMode = None
        for line in fpKey.readlines():
            if line[0] == '*':
                if line == '*version\n':
                    fileMode = 0
                elif line == '*threads\n':
                    fileMode = 1
                elif line == '*methods\n':
                    fileMode = 2
                elif line == '*end\n':
                    fileMode = 3
            else:
                if fileMode == 1: # thread
                    sp = line.split()
                    self.infoThreads[int(sp[0])] = sp[1]
                    pass
                elif fileMode == 2: # method
                    sp = line.split()
                    c = sp[1].replace('/', '.')
                    self.infoMethods[int(sp[0], 16)] = c + '.' + sp[2]
                    pass
        fpKey.close()

        fpData = open(self.fileData, 'rb')
        lid = 0
        if fpData.read(4) != 'SLOW':
            return False

        version = struct.unpack('H', fpData.read(2))[0]
        
        if version != 3 and version != 1:
            print 'error'
            return False
        
        offset = struct.unpack('H', fpData.read(2))[0]

        fpData.seek(offset)

        while(True):
            if version == 1:
                data = fpData.read(1)
                if data:
                    try:
                        idThread = struct.unpack('B', data)[0]
                        t = struct.unpack('I', fpData.read(4))[0]
                        modeMethod = t & 3
                        idMethod = t & 0xFFFFFFFC
                        timeCall = struct.unpack('I', fpData.read(4))[0]
                        if self.timeline < timeCall:
                            self.timeline = timeCall
                    except:
                        continue
                else:
                    break                
            elif version == 3:
                data = fpData.read(2)
                if data:
                    try:
                        idThread = struct.unpack('H', data)[0]
                        t = struct.unpack('I', fpData.read(4))[0]
                        modeMethod = t & 3
                        idMethod = t & 0xFFFFFFFC
                        timeCall = struct.unpack('I', fpData.read(4))[0]
                        #r = struct.unpack('I', fpData.read(4))[0]
                        fpData.read(4)
                        if self.timeline < timeCall:
                            self.timeline = timeCall
                    except:
                        continue
                else:
                    break
            key = (('%09u' % timeCall) + '-' + ('%09u' % lid))

            self.infoLog[key] = [ timeCall, idThread, idMethod, modeMethod ]
            lid = lid + 1
            
            key = self.infoMethods[idMethod]
            if modeMethod == 0: # method enter
                if not self.infoMethodCall.has_key(key):
                    self.infoMethodCall[key] = []
                    self.infoMethodCallEntry[key] = 0
                    self.infoMethodCall[key].append([ timeCall ])
                else:
                    self.infoMethodCall[key].append([ timeCall ])
            else:
                if not self.infoMethodCall.has_key(key):
                    pass
                else:
                    self.infoMethodCall[key][self.infoMethodCallEntry[key]].append( timeCall )
                    self.infoMethodCallEntry[key] = self.infoMethodCallEntry[key] + 1

        fpData.close()
        return True

    def outputLog(self, outFile = None, inFilterThreads = None, outFilterThreads = None):
        infoMode = ['enter', 'exit', 'e-exit']
        
        if outFile != None:
            fp = open(outFile, 'w')
        else:
            fp = sys.stdout
        
        for key in sorted(self.infoLog.keys()):
            timeCall = self.infoLog[key][0]
            idThread = self.infoLog[key][1]
            idMethod = self.infoLog[key][2]
            modeMethod = self.infoLog[key][3]
            if outFilterThreads != None and self.infoThreads[idThread] in outFilterThreads:
                pass
            elif inFilterThreads == None or self.infoThreads[idThread] in inFilterThreads:
                outString = ('%10u' % timeCall) + ' ' + ('%15s' % self.infoThreads[idThread]) \
                 + ('%8s' % infoMode[modeMethod]) + ' ' + self.infoMethods[idMethod] + '\n'
                fp.write(outString)

        if outFile != None:
            fp.close()

    def getMethodTime(self, methodName):
        try:
            return self.infoMethodCall[methodName]
        except:
            return None
    
    def getTimeline(self):
        return self.timeline

class methodView():
    def __init__(self):
        self.ax = None
        self.fig = None
        self.names = None
        self.timeline = None
        self.lineByName = {}
        pass

    def create(self, name, timeline, names):
        self.names = names
        self.timeline = timeline
        
        for nid in range(len(names)):
            self.lineByName[names[nid]] = nid
        
        height = len(names) + 1
        self.fig = plt.figure(figsize=(20, height), dpi=80) #()
        self.fig.canvas.set_window_title(name)
        self.ax = self.fig.add_subplot(111)
        pos = np.arange(len(names))+0.5
        pylab.yticks(pos, names)
        self.ax.axis([0, timeline, 0, height])
        plt.subplots_adjust(left=0.10, right=0.98, top = 0.95, bottom = 0.25)
        #plt.text(timeline/2, -0.2, 'TIMELINE', horizontalalignment='center', size='small')
        self.ax.set_xlabel('TIMELINE')
        
    def drawBar(self, name, x, color = 'r'):
        if self.lineByName.has_key(name):
            y = self.lineByName[name]
        else:
            print 'error'
            return
    
        pos = [ y + 0.5 ]
        self.ax.barh(pos, [x[1] - x[0]], align='center', height=0.6, color=color, left = [x[0]])

    def drawBars(self, name, xs, color = 'r'):
        if self.lineByName.has_key(name):
            y = self.lineByName[name]
        else:
            print 'error'
            return None
    
        sx = []
        w = []
        pos = []
        for x in xs:
            if len(x) == 2:
                sx.append(x[0])
                w.append(x[1] - x[0])
                pos.append( y + 0.5 )

        r = self.ax.barh(pos, w, align='center', height=0.6, color=color, left = sx)
        return r
    
    def drawCommit(self, rects, commits):
        plt.legend( rects, commits )
    
    def show(self):
        plt.show()

    def save(self, name):
        self.fig.canvas.print_figure(name)


class traceView:
    def __init__(self, sfile):
        self.trace = methodTrace()
        self.trace.openTraceFile(sfile)
        if not self.trace.parse():
            self.trace = None
        self.view = None
        
    def parseView(self, filters):
        if self.trace == None:
            return False
        figNames = []
        commitNames = {}
        for sfilter in filters:
            k = sfilter[1]
            v = k + ':' + sfilter[0].split('.')[-1]
            if not k in figNames:
                figNames.append(k)

            if not commitNames.has_key(k):
                commitNames[k] = [v]
            else:
                commitNames[k].append(v)
        
        commits = []
        for k in commitNames.keys():
            if len(commitNames[k]) == 1:
                del commitNames[k]
            else:
                commits = commits + commitNames[k]
        
        view = methodView()
        view.create('view', self.trace.getTimeline(), figNames)
        rs = []
        for fid in range(len(filters)):
            data = self.trace.getMethodTime(filters[fid][0])
            r = view.drawBars(filters[fid][1], data, filters[fid][2])
            k = filters[fid][1]
            if commitNames.has_key(k):
                rs.append(r[0])
    
        if len(rs) != 0:
            view.drawCommit(rs, commits)
            
        self.view = view
        return True

    def showView(self, filters):
        self.parseView(filters)
        if self.view != None:
            self.view.show()

    def saveLog(self, sfile = None, inFilters = None, outFilters = None):
        if self.trace != None:
            self.trace.outputLog(sfile, inFilters, outFilters)
            


if __name__ == '__main__':
    filters = [
            ['android.view.InputEventConsistencyVerifier.onTouchEvent', 'onTouchEvent', 'r'],
            ['android.os.MessageQueue.nativePollOnce', 'AP', 'r'],
            ['android.os.Handler.dispatchMessage', 'AP', 'y'],
            ['android.view.ViewRootImpl.finishInputEvent', 'AP2', 'y'],
            ['android.view.MotionEvent.recycle', 'AP2', 'r'],
            ]
    
    v = traceView('ddms.trace')
    v.showView(filters)
    #v.saveLog('log', None, ['FinalizerWatchdogDaemon', 'JDWP'])










