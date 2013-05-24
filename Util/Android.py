

from Util import util
import subprocess


class android():
    def __init__(self):
        self.logcatPopen = None
    
    def install(self, apk):
        util.run('adb install -r ' + apk)
        
    def uninstall(self, apk):
        pass
    
    def startLogcat(self, wfile):
        outFile =  open(wfile, 'w')
        cmd = 'adb logcat -v threadtime'
        logcat = subprocess.Popen(cmd, stdout=outFile, stderr=outFile, universal_newlines=False, shell=True)

        self.logcatPopen = logcat
    
    def stopLogcat(self):
        if self.logcatPopen != None:
            self.logcatPopen.terminate()
            self.logcatPopen = None