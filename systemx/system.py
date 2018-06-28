import platform
import socket
import pwd
import sys
import os

# Dependecies that aren't installed by default
try:
	import requests
except ImportError:
	print("Failed to import the 'requests' module. Please install by typing in a terminal: 'sudo pip install requests' or 'sudo pip3 install requests'.")
	print("pip3 is for Python 3")

username = pwd.getpwuid(os.getuid()).pw_name

if platform.system() == "Darwin" or "darwin":
	operating_system = []
	operating_system.append("macOS")
	operating_system.append(platform.mac_ver()[0])
	
ip_address = []
ip_address.append([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
ip_address.append(requests.get('https://api.ipify.org').text.encode("ascii"))
