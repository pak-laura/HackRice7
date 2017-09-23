'''
Created on Sep 23, 2017

@author: tuvan
'''
import tweepy
import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import csv

apple_words= ['Apple', 'iPhone', 'iPad', 'Mac', 'iOS']


#modify Streamlistener to print out stream
#definition here: https://github.com/tweepy/tweepy/blob/master/tweepy/streaming.py
class MyStreamListener(StreamListener):

    #initialize values
    def __init__(self, api=None, start_time = time.time(), time_limit = 5):
        self.api = api
        self.start = start_time
        self.end = time_limit+start_time
        self.tweets = [] #stores all data to add to file
        
    #what happens on each iteration
    def on_status(self, data):
  
        
        while (time.time() <self.end): 
            self.tweets.append([data.text])
            print(data.text)
            return True #somehow stops program from reprinting same tweet
        
        #csv_file = open("Twitter_Stream.csv",'w', newline = ' ', encoding = 'utf-8') 
        #writer = csv.writer()
#         for tweet in self.tweets:
#             writer.writerow(tweet)
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

#Create OAuthHandler instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Create stream listener
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

#filters out tweets with keywords and in english
myStream.filter(track=apple_words, languages = ['en'])



# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)