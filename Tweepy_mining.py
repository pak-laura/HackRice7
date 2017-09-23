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


from keys import * 
#replace with values for
#consumer_key =
#consumer_secret =
# access_token =
#access_token_secret =

#modify Streamlistener to print out stream
#definition here: https://github.com/tweepy/tweepy/blob/master/tweepy/streaming.py
class MyStreamListener(StreamListener):
    #initialize values
    def __init__(self, filename, start_time=time.time(), api=None, time_limit = 5):
        self.api = api
        self.start = start_time
        self.end = time_limit+start_time
        self.tweets = [] #stores all data to add to file
        self.file = filename
        
    #what happens on each iteration
    def on_status(self, status):
        while (time.time() <self.end): 
            self.tweets.append(status)
            print("Getting tweet from %s" %(status._json['user']['screen_name']))
            return True #somehow stops program from reprinting same tweet
        
        with open(self.file, 'w', newline='', encoding = 'utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for tweet in self.tweets:
                writer.writerow([tweet._json['user']['screen_name'], tweet._json['text'],
                                tweet._json['retweet_count']])
                print('@%s tweeted: %s' %(tweet._json['user']['screen_name'], tweet._json['text']))
        return False       
       
    #prevents rate limiting
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

#Create OAuthHandler instance

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

apple_words= ['Apple', 'iPhone', 'iPad', 'Mac', 'iOS']
google_words = ['Google','google','gmail']
microsoft_words = ['Microsoft', 'microsoft', 'windows', 'powerpoint', 'xbox']
samsung_words = ['android', 'galaxy tab', 'samsung']

stream_length = 60 #in seconds

#Create stream listeners and filters
#languages = ['en'] for English tweets only
#async = True parameter ensures the stream will run on a new thread
AppleListener = MyStreamListener(filename = 'Apple.csv', time_limit = stream_length)
AppleStream = tweepy.Stream(auth = api.auth, listener=AppleListener )
AppleStream.filter(track=apple_words, languages = ['en'], async=True)

GoogleListener = MyStreamListener(filename = 'Google.csv', time_limit = stream_length)
GoogleStream = tweepy.Stream(auth = api.auth, listener=GoogleListener )
GoogleStream.filter(track=google_words, languages = ['en'], async = True)

MicrosoftListener = MyStreamListener(filename = 'Microsoft.csv', time_limit = stream_length)
MicrosoftStream = tweepy.Stream(auth = api.auth, listener=MicrosoftListener )
MicrosoftStream.filter(track=microsoft_words, languages = ['en'], async = True)

SamsungListener = MyStreamListener(filename = 'Samsung.csv', time_limit = stream_length)
SamsungStream = tweepy.Stream(auth = api.auth, listener=SamsungListener )
SamsungStream.filter(track=samsung_words, languages = ['en'], async = True)

