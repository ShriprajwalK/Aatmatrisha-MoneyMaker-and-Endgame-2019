from bs4 import BeautifulSoup
import requests
import time


j=1
source = requests.get('http://10.9.90.29:8000/').text
soup = BeautifulSoup(source, 'lxml')
    #print(soup.prettify())
def write():
	with open("/var/www/html/scrape_info.txt", 'w') as f:
		if check>0:
        		f.writelines("")


td = soup.find_all("td")
s = ""
for i in range(1,len(td),3):
    s += str(str(j)+","+str(td[i].text).strip())+"\n"

with open("/var/www/html/scrape_info.txt",'a') as f:
    f.writelines(s)

check = 0 
with open("/var/www/html/scrape_info.txt", 'r') as f:
	if len(f.readlines())>=384:
		write()

j+=1
