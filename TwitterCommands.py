
#API setup and import
import datetime
import tweepy
import random
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from TwitterAPIKeys import API
import time


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
    page = 1
    user = API.get_user(username)
    tweets = API.user_timeline(screen_name = username, count = 150, include_rts = True, tweet_mode='extended', page=page)
    
    list_of_tweets = []
    for tweet in tweets:
        if (start <= tweet.created_at) and (end >= tweet.created_at):
            list_of_tweets.append(tweet.full_text)
    page = 2
    deadend = False
    while not deadend:
        tweets = API.user_timeline(screen_name=username, count = 150,include_rts = True, tweet_mode='extended', page = page)
        if tweets == []:
            deadend = True
            continue
        for tweet in tweets:
            print(tweet.created_at)
            if (start <= tweet.created_at) and (end >= tweet.created_at):
                #Do processing here:
                list_of_tweets.append(tweet.full_text)
            if (start > tweet.created_at):
                deadend = True
                continue
        if not deadend:
            page += 1
    print('done')
    print(list_of_tweets)
    return list_of_tweets


'''
returns a list of tweets with the given hashtag in them.
paramaters:
        string hashtag (the hashtag given to search tweets for)
        datetime start (the date to start looking for tweets from)
return type: list[] (of tweets)
'''
def getHashtagTweets(hashtag, start):
    page = 1
    list_of_tweets = []
    for tweet in tweepy.Cursor(API.search, q=hashtag, rpp=150, lang="en", since=start, count=150).items():
        list_of_tweets.append(tweet.text)
    return list_of_tweets

#____________________________________________________________

if __name__ == '__main__':
    
    start = datetime.datetime(2016, 1, 1, 0, 0)
    end = datetime.datetime(2019, 12, 31, 23, 59)
    '''
    list_ = getUserTweets("realdonaldtrump", start, end)
    for i in list_:
        print i, "\n\n"
    #list2 = getHashtagTweets("#cool", start, end, 15)
    #for i in list2:
     #   print i, "\n\n"
     '''
    x = getHashtagTweets("#fun", start)
    for i in x:
        print (i)