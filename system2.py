import platform
import pwd
import sys
import os

plat = platform.system()

def username():
    return pwd.getpwuid(os.getuid()).pw_name

def operating_system():
    if plat == "Darwin" or "darwin":
      os_return = []
      os_return.append("macOS")
      os_return.append(platform.mac_ver()[0])
      return os_return
