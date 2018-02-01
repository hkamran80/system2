import platform
import pwd
import sys
import os

plat = platform.system()

class System():
    global plat

    def username(self):
        return pwd.getpwuid(os.getuid()).pw_name
    
    def operating_system(self):
        if plat == "Darwin" or "darwin":
        	os_return = []
        	os_return.append("macOS")
        	os_return.append(platform.mac_ver()[0])
        	return os_return
