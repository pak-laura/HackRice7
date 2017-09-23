from TwitterSearch import *
import csv

apple_words = ['Apple','iPhone','iPad','Mac','Apple Watch']

try:
	tso = TwitterSearchOrder()
	tso.set_keywords(apple_words)
	tso.set_language('en')
	tso.set_result_type('mixed')
	tso.set_count(100)

	ts = TwitterSearch(
	)
	
	with open('searchT.csv','w',newline='') as f:
		wrote = csv.writer(f)
		for tweet in ts.search_tweets_iterable(tso):
			wrote.writerow([tweet['user'],tweet['text'],tweet['retweet_count'],tweet['created_at']])
except TwitterSearchException as e:
		print(e)
