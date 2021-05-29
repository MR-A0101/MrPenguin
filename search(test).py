from youtube_search import YoutubeSearch
import requests
import json
import random
#results = YoutubeSearch("Come and Go", max_results = 5,).to_dict()

requests = requests.get("https://animechan.vercel.app/api/quotes/anime?title=naruto")
#load = json.loads(requests)
number = random.randint(0,10)
#print(number)
#print(requests.json())
print(requests.json()[number]["quote"])
print('- ' + requests.json()[number]["character"])
#for i in requests.text:
#	print(i)
#print(requests.text)
#for i in results:
#	print(i['title'], end = " ")
#	print(i['url_suffix'],)
	
#	r = requests.get("www.youtube.com" + "{0}['url_suffix']".format(i))
#	print(r)
#
#	print()
#	print()
#rint(type(results))


