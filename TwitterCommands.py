
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
    tweets = API.user_timeline(screen_name = username, count = user.statuses_count, include_rts = True, tweet_mode="extended")
    list_of_tweets = []
    
    #grab all of the random tweets made by the user.
    i = 0
    while i < len(tweets) and len(list_of_tweets) <= sample_size:
        random_tweet = random.choice(tweets)
        if (random_tweet not in list_of_tweets) and (start <= random_tweet.created_at) and (end >= random_tweet.created_at):
            list_of_tweets.append(random_tweet)
        i += 1
    #go throuvgh the list of tweet objects and parse out all of the tweet.text
    #take all of that and add it to a list
    #return the list of tweet text right after
    list_of_tweet_text = [[tweet.full_text] for tweet in list_of_tweets]
    return list_of_tweet_text

'''
go through all the searches for a givn hashtag.
paramaters:
        string hashtag(twitter hashtag)
        string start(beginning time range to grab tweet from)
        string end(ending time range to grab tweet from)
        int sample_size( amount of tweets you want to grab)
return type: list[] (of tweets as text)    

'''
def getHashtagTweets(hashtag, start, end, sample_size):
    search_results = API.search(hashtag)
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



start = datetime.datetime(2016, 1, 1, 0, 0)
end = datetime.datetime(2019, 12, 31, 23, 59)
list_ = getUserTweets("realdonaldtrump", start, end, 15)

list2 = getHashtagTweets("#cool", start, end, 15)
for i in list2:
    print i, "\n\n"