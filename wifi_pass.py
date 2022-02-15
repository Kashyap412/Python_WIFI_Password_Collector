import subprocess,csv
from datetime import datetime
from time import sleep


def Banner(a):
	print("\n"+"#"*65)
	print("#\tWelcome to KashY "+a+"\t#\n#\t\t\t\t\t\t\t\t#")
	print("#\tTime started at\t: "+str(datetime.now())+"\t\t#\n#\t\t\t\t\t\t\t\t#")
	print("#\tCheck wifi-passwords.csv file for Wifi Passwords\t#")
	print("#"*65+"\n\n")

Banner("WiFi Password Extractor for Windows")

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n') 
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]


header =["Network Name","Password"]
f = open('wifi-passwords.csv', 'w')
writer = csv.writer(f)
writer.writerow(header)
f.close()
for i in profiles:
	try: 
		results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n') 
		results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
		
		try:
			
			da = [i,results[0]]
			f = open('wifi-passwords.csv', 'a')
			writer = csv.writer(f)
			writer.writerow(da)
			f.close()
		except IndexError:
			pass
	except subprocess.CalledProcessError:
		pass


