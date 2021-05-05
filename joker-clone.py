import requests
import sys
import socket
import os
import re
import time
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
#cores
vd='\033[32m'
am='\033[33m'
vm='\033[31m'
az='\033[36m'
ng='\033[1m'
f='\033[m'
lz='\033[34m'

os.system("clear")

print(f"""{f}{lz}

🃏script simples para clone!!@bydeathlxncer🃏
 _         _         _   _   _                     
| |_ _ _ _| |___ ___| |_| |_| |_ _ ___ ___ ___ ___ 
| . | | | . | -_| .'|  _|   | |_'_|   |  _| -_|  _|
|___|_  |___|___|__,|_| |_|_|_|_,_|_|_|___|___|_|  
    |___|                                          
{f}""")
time.sleep(2)
os.system("clear")

def download(item):

	global downloadedFiles

	if any(s in item for s in dataTypesToDownload):

		if " " in item:  # https://stackoverflow.com/a/4172592
			return

		while item.startswith("/"):
			item = item[1:]

		external = False
		prefix = ""

		if "#" in item:
			item = item.split("#")[0]
		
		if item.startswith("https://"):
			external = True
			prefix = "https://"
			item = item.replace("https://", "")
			
		if item.startswith("http://"):
			external = True
			prefix = "http://"
			item = item.replace("http://", "")

		if item.startswith("../"):
			item = item.replace("../", "dotdot/")

		if item in downloadedFiles:
			return

		try:
			item_path = item.split("/")
			
			if len(item_path) != 1:
				item_path.pop(len(item_path) - 1)
				trail = "./" + base_path + "/"
				for folder in item_path:
					trail += folder+"/"
					try:
						os.mkdir(trail)
					except OSError:
						pass	

		except IOError:
			pass

		try:

			if "?" in item:
				download = open(base_path + "/" + item.split("?")[len(item.split("?")) - 2], "wb")
			else:
				download = open(base_path + "/" + item, "wb")

			print("baixando {} para {}".format(item, download.name))

			if external:
				dContent = requests.get(prefix+item, stream=True)
			else:
				dContent = requests.get(url+"/"+item, stream=True)
		
		except Exception as e:
		
			print(f"{f}{vd}um erro ocorreu:{f} " + str(e.reason))
			download.close()
			return
		
		for chunk in dContent:
			download.write(chunk)

		download.close()
		print("baixado!")
		downloadedFiles.append(resource)
socket.setdefaulttimeout(15)
downloadedFiles = []
dataTypesToDownload = [".jpg", ".jpeg", ".png", ".gif", ".ico", ".css", ".js", ".html", ".php", ".json", ".ttf", ".otf", ".woff", ".eot"]
print(f"""{am}
               _
              (_)          _
          _         .=.   (_)
         (_)   _   //(`)_
              //`\/ |\ 0`\\
              ||-.\_|_/.-||
              )/ |_____| \(    _
             0   |/\ /\|  0   (_)
                _| o o |_
         _     ((|, ^ ,|))
        (_)     `||\_/||`
                 || _ ||      _
                 | \_/ |     (_)
             0.__.\   /.__.0
              `._  `"`  _.'
                 / ;  \ \

 ▄▄▄██▀▀▀▒█████   ██ ▄█▀▓█████  ██▀███  
   ▒██  ▒██▒  ██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
   ░██  ▒██░  ██▒▓███▄░ ▒███   ▓██ ░▄█ ▒
▓██▄██▓ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
 ▓███▒  ░ ████▓▒░▒██▒ █▄░▒████▒░██▓ ▒██▒
 ▒▓▒▒░  ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░▒░    ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░ ░  ░ ░ ░ ▒  ░ ░░ ░    ░     ░░   ░ 
 ░   ░      ░ ░  ░  ░      ░  ░   ░     
   {f}{lz} palhaço do mau clonador de sites{f}
{f}{am}nota:dependendo do tamanho do site o script não vai clonar.{f}
              {f}{lz} @bydeathlxncer{f}""")


if len(sys.argv) == 1:
	url = input(f"{f}{az}{f}{lz}{f}{az}{f}{vd}url do site a ser clonado:{f} ")
else:
	if sys.argv[1] == "-h":
		print("uso: {} [url] [directory]".format(sys.argv[0]))
		exit()
	url = sys.argv[1]

if len(sys.argv) <= 2:
	base_path = input(f"{f}{az}{f}{lz}{f}{az}{f}{vd}diretório para clonar em:{f} ")
else:
	base_path = sys.argv[2]

if "http://" not in url and "https://" not in url:
	url = "http://"+url

domain = "//".join(url.split("//")[1:])

try:
	os.mkdir(base_path)
except OSError:
	pass

with requests.Session() as r:
	try:
		content = r.get(url).text
	except Exception as e:
		print("erro: {}".format(e))

file = open(base_path + "/index.html", "w", encoding='utf-8')
file.write(content.replace('src="https://', 'src="'))
file.close()

resources = re.split("=\"|='", content)

for resource in resources:

	resource = re.split("\"|'", resource)[0]

	download(resource)

# capture documentos de nível raiz em tag href
hrefs = content.split("href=\"")

for i in range( len(hrefs) - 1 ):
	href = hrefs[i+1]
	href = href.split("\"")[0]
	if "/" not in href and "." in href and ("." + href.split(".")[-1]) in dataTypesToDownload:
		download(href)

textFiles = ["css", "js", "html", "php", "json"]
print(f'{f}{vd}procurando referências de url(x) baseada em CSS...{f}')

for subdir, dirs, files in os.walk(base_path):
	for file in files:
		
		if file == ".DS_Store" or file.split(".")[-1] not in textFiles:
			continue

		f = open(os.path.join(subdir, file), 'r', encoding='utf-8')
		
		content = f.read()
		if "url(" in content:
			arr = content.split("url(")
			iterations = len(arr) - 1
			i = 1
			for x in range(iterations):
				path = arr[i].split(")")[0]
				download(path)
				i += 1
			
print(f"{f}{vd}clonado, se você da o comando (ls) vai aparecer a pasta com o nome de (diretorio) que você colocou para mover a pasta use o comando (mv (nome do diretorio que você colocou) /sdcard/Download) a pasta será movida📁.{f} "+url+" !")
