#!/usr/bin/python3
from youtube_search import YoutubeSearch
import pafy
import os
import pandas as pd
import time

os.system('clear')
def search(term):
	failurerate = 0
	success = 0
	starttime = time.time()
	links = []

	results = YoutubeSearch( term, max_results=40).to_dict()
	for key in results:
		dicty = key 
		if len(dicty['id']) < 12:
			links.append('https://youtube.com'+dicty['link'])

	titles = []
	durations = []
	views = []
	print("results found, formatting for readability... lol")
	for i in links:
		try:
			v = pafy.new(i)
			titles.append(v.title)
			durations.append(v.duration)
			views.append(v.viewcount)
			success +=1

		except Exception:
			failurerate+=1

	table = {"title": titles, "duration": durations, "views": views}
	df = pd.DataFrame(table)
	print(failurerate, "fails", success, "sucesses" )
	print(df)	

	def time_convert(sec):
	  mins = sec // 60
	  sec = sec % 60
	  hours = mins // 60
	  mins = mins % 60
	  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

	endtime = time.time()
	time_lapsed = endtime - starttime
	time_convert(time_lapsed)

	return links



