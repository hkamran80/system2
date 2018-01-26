import platform
import pwd
import sys
import os

plat = platform.system()

class System():
    global plat

    def username(x):
        return pwd.getpwuid(os.getuid()).pw_name
    
    def operating_system(x):
        if plat == "Darwin" or "darwin":
        	os_return = []
        	os_return.append("macOS")
        	os_return.append(platform.mac_ver()[0])
        	return os_return
       	elif plat == "":
       		print "NULL"