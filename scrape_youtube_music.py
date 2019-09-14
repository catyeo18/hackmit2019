import requests 
from bs4 import BeautifulSoup 
import json
  
url = 'https://www.youtube.com/playlist?list=RDCLAK5uy_ktU_MiPyxsoBpl68TuShAvg-ZCArB772M'
data = requests.get(url)
# print(data)
  
soup = BeautifulSoup(data.content, 'html.parser') 
for itemName in soup.find_all("tr", attrs={'class':"pl-video yt-uix-tile "}):
	print(itemName["data-title"])
	print(itemName["data-video-id"])
  
# print(content)

videoID=[]  