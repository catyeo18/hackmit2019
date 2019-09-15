import requests 
from bs4 import BeautifulSoup 
import csv 
import random
  
def return_playlist():
	return 



# Input: Youtube Playlist URL
def return_track(emotion):
	URL = "https://youtube.com/playlist?list=RDCLAK5uy_kJWGcrtTC_zrbD6rKkBvOcht_vzijhX1A"
	r = requests.get(URL) 
	soup = BeautifulSoup(r.content, 'html.parser') 
	# print(soup)
	  
	urls=[]  

	# print(soup.findAll('tr', attrs = {'class':'pl-video yt-uix-tile'}))

	for row in soup.findAll('tr', attrs = {'class':'pl-video yt-uix-tile '}):
	    urls.append(row["data-video-id"])

	part = random.choice(urls)
	url = "https://www.youtube.com/watch?v=" + part

	return(url)