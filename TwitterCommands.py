
#API setup and import
import datetime
import tweepy
import random
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from TwitterAPIKeys import API


'''
returns a list of a bunch of random tweets#
made by one specific user 
paramaters:
    string username(twitter username)
    string start(beginning time range to grab tweet from)
    string end(ending time range to grab tweet from)
    int sample_size( amount of tweets you want to grab)
return type: list[] (of tweets as text)    
'''
def getUserTweets(username, start, end, sample_size):
    user = API.get_user(username)
    tweets = API.user_timeline(screen_name = username, count = user.statuses_count, include_rts = True)
    list_of_tweets = []
    
    #grab all of the random tweets made by the user.
    i = 0
    while i < len(tweets) and len(list_of_tweets) <= sample_size:
    	random_tweet = random.choice(tweets)
    	tweet = tweets[i]
    	if (random_tweet not in list_of_tweets) and (start <= tweet.created_at) and (end >= tweet.created_at):
    		print(tweet.created_at, tweet.text, "\n")
    		list_of_tweets.append(random_tweet)
    	i += 1

    #go through the list of tweet objects and parse out all of the tweet.text
    #take all of that and add it to a list
  	#return the list of tweet text right after
    list_of_tweet_text = []
    print len(list_of_tweets)
    for i in range(len(list_of_tweets)):
    	list_of_tweet_text.append(list_of_tweets[i].text)
    	print len(list_of_tweets)

   	return list_of_tweet_text


'''
#connect to the tweepy api
auth = tweepy.OAuthHandler(CK, SK)
auth.set_access_token(AT, ST)
requestToken(auth)
api = tweepy.API(auth)
'''

start = datetime.datetime(2016, 1, 1, 0, 0)
end = datetime.datetime(2019, 12, 31, 23, 59)
print start
print end
list_ = getUserTweets("realdonaldtrump", start, end, 15)
print len(list_)