

from Util import util
import subprocess


class android():
    def __init__(self):
        self.logcatPopen = None
        self.logcatFile = None
    
    def install(self, apk):
        util.run('adb install -r ' + apk)
        
    def uninstall(self, apk):
        pass
    
    def startLogcat(self, wfile):
        outFile =  open(wfile, 'w')
        cmd = 'adb logcat -v threadtime'
        logcat = subprocess.Popen(cmd, stdout=outFile, stderr=outFile, universal_newlines=False)

        self.logcatPopen = logcat
        self.logcatFile = outFile
    
    def stopLogcat(self):
        if self.logcatPopen != None:
            self.logcatPopen.terminate()
            print 'stop'
            self.logcatPopen = None
            self.logcatFile.close()
            self.logcatFile = None
    
    def filterLogcat(self, ifile, ofile, tags):
        rfile = open(ifile, 'r')
        lines = rfile.readlines()
        rfile.close()
        
        wfile = open(ofile, 'w')
        for line in lines:
            rep = False
            for tag in tags:
                if line.find(tag) > -1:
                    rep = True
                    break
            if rep == True:
                line = line.replace('\r', '')
                wfile.write(line)
                
        
        wfile.close()
        
        
        
        
        
        
        
        
        
        
        