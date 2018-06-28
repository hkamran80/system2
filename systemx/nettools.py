# NetTools for Python

#from warnings import filterwarnings
import subprocess
#import ipwhois

#filterwarnings(action="ignore")

def get_base_ip():
	ipconfig = subprocess.Popen("ifconfig en0".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]

	if "inet" in ipconfig.decode("utf-8").split("\n")[-5] and "inet6" not in ipconfig.decode("utf-8").split("\n")[-5]:
		return ".".join(ipconfig.decode("utf-8").split("\n")[-5].split(" ")[1].split(".")[n] for n in range(0, 3))

def clean_ip(ip):
	return ".".join([ip[-int(n)] for n in range(1, 5)])

def nslookup(ip):
	try:
		cmd = subprocess.Popen(["nslookup", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode("utf-8").replace("\t", "").split("\n")

		#try:
		#	whois_data = ipwhois.IPWhois(ip).lookup_whois()["nets"][0]["name"]
		#except ipwhois.exceptions.WhoisLookupError:
		#	whois_data = "unavailable"

		return {"ip":clean_ip(cmd[4].split(" = ")[0].split(".")[:-2]), "hostname":cmd[4].split(" = ")[1][:-1]}#, "owner":whois_data}
	except IndexError:
		return subprocess.Popen(["nslookup", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode("utf-8").replace("\t", "").split("\n")[-3]
		#return subprocess.Popen(["nslookup", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[1].decode("utf-8")
