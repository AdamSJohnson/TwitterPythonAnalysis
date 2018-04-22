
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
        print(page)
        tweets = API.user_timeline(screen_name=username, count = 150,include_rts = True, tweet_mode='extended', page = page)
        print(len(tweets))
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
            page+=1
            #time.sleep(50)
    print('done')
    print(list_of_tweets)
    return list_of_tweets


'''
def getHashtagTweets(hashtag, start, end, sample_size):
    search_results = API.search(hashtag, text_mode="full_text")
    list_of_tweets = []

    i = 0
    while i < len(search_results) and len(list_of_tweets) <= sample_size:
        random_tweet = random.choice(search_results)
        if (random_tweet not in list_of_tweets) and (start <= random_tweet.created_at) and (end >= random_tweet.created_at):
            list_of_tweets.append(random)
        i += 1

    list_of_tweet_text = []
    for i in list_of_tweets:
        list_of_tweet_text.append(i.text)
    return list_of_tweet_text
'''

'''
#____________________________________________________________
start = datetime.datetime(2016, 1, 1, 0, 0)
end = datetime.datetime(2019, 12, 31, 23, 59)
list_ = getUserTweets("realdonaldtrump", start, end)
for i in list_:
    print i, "\n\n"
#list2 = getHashtagTweets("#cool", start, end, 15)
#for i in list2:
 #   print i, "\n\n"
 '''