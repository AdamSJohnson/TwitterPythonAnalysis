
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
return type: list[] (of tweets as text)    
'''
def getUserTweets(username, start, end):
    date_start = datetime.datetime.strptime('01Jan' + str(start), '%d%b%Y') 
    date_end = datetime.datetime.strptime('01Jan' + str(end), '%d%b%Y')
    user = API.get_user(username)
    tweets = API.user_timeline(screen_name = username, count = user.statuses_count, include_rts = True, tweet_mode="extended")
    list_of_tweets = []
    for tweet in tweets:
        if (date_start <= tweet.created_at) and (date_end >= tweet.created_at):
            list_of_tweets.append(tweet.full_text)
    return list_of_tweets



def getHashtagTweets(hashtag, start, end):
    search_results = API.search(hashtag, rpp=2000)
    for i in search_results:
        print i.text, "\n\n"


#____________________________________________________________
start = datetime.datetime(2016, 1, 1, 0, 0)
end = datetime.datetime(2019, 12, 31, 23, 59)
list_ = getUserTweets("realdonaldtrump", 2016, 2017)
for i in list_:
    print i, "\n\n"
#list2 = getHashtagTweets("#cool", start, end, 15)
#for i in list2:
 #   print i, "\n\n"
 #getHashtagTweets