import requests
from bs4 import BeautifulSoup

URL = "https://bot-not-not-bot.vishwactf.com/"
print("Sending request to : ", URL)
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links[0])

for link in links:
	inner_url = URL+link
	inner_req = requests.get(inner_url)
	print("Sending request to : ", inner_url)
	inner_soup = BeautifulSoup(inner_req.content, 'html5lib')
	if inner_soup.select('h1'):
		print(inner_soup.select('h1'), " : ", print(inner_soup.select('p')))