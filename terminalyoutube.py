from youtube_search import YoutubeSearch
import os
import signal

amount = 20
os.system('clear')
global defaultvalue
defaultvalue = 'jazz'

class player:
	
	def __init__(self):
		print('base loaded')

	def search(searchterm, default):
		if len(searchterm) == 0:
			print("user input empty, defauting to "+ default+ " music")
			results = results = YoutubeSearch( default, max_results=amount).to_dict()

		else:
			results = YoutubeSearch(searchterm, max_results=amount).to_dict()

		r = 0
		videoid = []
		for key in results:
		    dicty = key 
		    if len(dicty['id']) < 12:
		        r+=1
		        print(r, dicty['title'])
		        videoid.append('https://youtube.com'+dicty['link'])
		    else:
		        print('')

		urllist = videoid
		return urllist

	def play(urllist, choice):
		choice-=1
		url = urllist[choice]
		os.system('mpv '+ url +' --no-video')
		os.system('rm -rf ~/.cache/youtube_dl')

def main():

	def stringornot(value):
		
		try:
			int(value)
			return 'int'

		except ValueError:
			return 'string'

	def switch(term, choice):
		if stringornot(choice) == 'int':
			choice = int(choice)
			os.system('clear')
			player.play(player.search(term, defaultvalue), choice)
		else:
			return

	integer = False
	while integer == False:
		term = input('=> ')

		player.search(term, defaultvalue)
		choice = input('=> ')
		switch(term, choice)

		if stringornot(choice) == 'int':
			integer = True
			while integer == True:
				next = input('<=> ')
				if stringornot(next) == 'string':
					print('sorry you need to search that term')
					integer = False
				else:
					switch(term, next)

		else:
			integer = False			
		
		

def keyboardInterruptHandler(signal, frame):
	os.system('clear')
	exit()

signal.signal(signal.SIGINT, keyboardInterruptHandler)

while True:
	main()
