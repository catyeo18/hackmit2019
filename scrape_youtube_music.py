import requests 
from bs4 import BeautifulSoup 
import csv 
import random
  

# Input: Youtube Playlist URL
def return_track(emotion):
	# URL = "https://youtube.com/playlist?list=RDCLAK5uy_kJWGcrtTC_zrbD6rKkBvOcht_vzijhX1A"
	
	# happyURL = "https://youtube.com/playlist?list=RDCLAK5uy_kJWGcrtTC_zrbD6rKkBvOcht_vzijhX1A"
	# sadURL = "https://youtube.com/playlist?list=RDCLAK5uy_kIlNbVLt0zdMDvQJgf9Ilzbpy9KSk1xE4"
	# angryURL
	# neutralURL = "https://www.youtube.com/playlist?list=RDCLAK5uy_kb7EBi6y3GrtJri4_ZH56Ms786DFEimbM"
	
	if emotion == 'HAPPY' or emotion == 'POSITIVE':
		URL = "https://www.youtube.com/playlist?list=PLhGO2bt0EkwvRUioaJMLxrMNhU44lRWg8"
	elif emotion == 'SAD' or emotion == 'NEGATIVE':
		URL = "https://youtube.com/playlist?list=RDCLAK5uy_kIlNbVLt0zdMDvQJgf9Ilzbpy9KSk1xE4"
	elif emotion == 'ANGRY':
		URL = 'https://www.youtube.com/playlist?list=RDCLAK5uy_mPqT1su7A0jeg2kTWdhj7I6JyDfwD4O-4'
	else:
		URL = "https://www.youtube.com/playlist?list=RDCLAK5uy_kb7EBi6y3GrtJri4_ZH56Ms786DFEimbM"


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