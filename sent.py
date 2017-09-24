'''citation for VADER sentiment analysis: Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.'''

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import csv
import pandas
import re

fileCo = 'Google.csv'
colnames = ['user','text','date']
data = pandas.read_csv(fileCo,names=colnames)
listText = data.text.tolist()
listDate = data.date.tolist()
sent_analyzer = SentimentIntensityAnalyzer()

pos_count=0
neg_count=0
neu_count=0
total_count=0
date0 = listDate[0][4:10]
with open('results.csv', 'w', newline='') as csvfile:
	wrote = csv.writer(csvfile)

	for tweet, date in zip(listText, listDate):
		if date[4:10] != date0: #new date
			wrote.writerow([date[4:10], pos_count/total_count, neg_count/total_count, neu_count/total_count])
			pos_count=0
			neg_count=0
			neu_count=0
			total_count=0
			date0 = date[4:10]

		ss = sent_analyzer.polarity_scores(tweet)
		if ss['compound'] > 0:
			pos_count += 1
		elif ss['compound'] < 0:
			neg_count += 1
		else:
			neu_count += 1
		total_count += 1

#	print(tweet)
#	for k in sorted(ss):
	#	k = compound,neg,neu,pos, ss[k] = some number
#		print('{0}: {1}, '.format(k,ss[k]),end ='')
#	print() #adds newline after scores print
'''
print("Positive tweets: ",pos_count/total_count,"%")
print("Negative tweets: ",neg_count/total_count,"%")
print("Neutral tweets: ",neu_count/total_count,"%")
print("total tweets: ",total_count)
'''



