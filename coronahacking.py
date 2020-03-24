#pip install --upgrade git+https://github.com/m-wrzr/populartimes
#pip install apscheduler
import populartimes
import json
from apscheduler.schedulers.blocking import BlockingScheduler

#https://developers.google.com/places/place-id?hl=de
#https://github.com/pkreissel/social_distance/blob/master/places.py
#https://github.com/m-wrzr/populartimes


def log_supermarkets():
	print("Started Data Collection")
	api_key = ""
	with open('supermarkets.json') as f:
	  supermarkets = json.load(f)

	supermarkets = supermarkets[0]
	#supermarkets = json.loads("supermarkets.json")[0]
	for market_name in supermarkets:
		google_key = supermarkets[market_name]
		data = populartimes.get_id(api_key, google_key)
		print(data)
		file_object = open(market_name + '.txt', 'a')
		if "current_popularity" in data:
			current_popularity = data["current_popularity"]
			print(market_name + ": " + str(current_popularity))
			file_object.write(str(current_popularity)+"\n")
		else:
			print("No popularity record for " +  market_name)
			file_object.write("-1\n")
		file_object.close()

scheduler = BlockingScheduler()
scheduler.add_job(log_supermarkets, 'interval', hours=1)
scheduler.start()

