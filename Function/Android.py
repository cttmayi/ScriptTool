

from Util.Util import util
import subprocess


class android():
    def __init__(self, frame):
        self.logcatThread = None
        self.logcatFile = None
        self.frame = frame
    
    def install(self, apk):
        util.run('adb install -r ' + apk)
        
    def uninstall(self, apk):
        pass
    
    def clearLogcat(self):
        cmd = 'adb logcat -c'
        util.run(cmd)
    
    def startLogcat(self, wfile):
        outFile =  open(wfile, 'w')
        cmd = 'adb logcat -v threadtime'

        logcatThread = self.frame.runCmdCbk(cmd, None, self.__onLogcatLine)

        self.logcatThread = logcatThread
        self.logcatFile = outFile


    def __onLogcatLine(self, line):
        if self.logcatFile != None:
            line = line.replace('\r', '')
            self.logcatFile.write(line)
        

    
    def stopLogcat(self):
        if self.logcatThread != None:
            self.logcatThread.stop()
            self.logcatThread = None
            self.logcatFile.close()
            self.logcatFile = None
            return True
        return False
    
    def touchLogcat(self):
        if self.logcatFile != None:
            self.logcatFile.write('>>> >>>\n')
        pass
        
    def filterLogcat(self, ifile, ofile, tags, pids = None):
        rfile = open(ifile, 'r')
        lines = rfile.readlines()
        rfile.close()
        
        for i in range(len(tags)):
            tags[i] = tags[i] + ':'
        
        
        wfile = open(ofile, 'w')
        for line in lines:
            words = line.split(None, 6)
            if len(words) == 7:
                rep = False

                for tag in tags:
                    #if line.find(tag) > -1:
                    if words[5] == tag: 
                        rep = True
                        break
                if pids != None and rep == False:     
                    for pid in pids:
                        #if line.find(tag) > -1:
                        if words[3] == pid: 
                            rep = True
                            break
                    
            else:
                rep = True
            if rep == True:
                line = line.replace('\r', '')
                wfile.write(line)
                
        
        wfile.close()
        
        
        
        
        
        
        
        
        
        
        