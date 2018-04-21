
#API setup and import
import datetime
import tweepy
import random
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from TwitterAPIKeys import CONSUMER_KEY as CK
from TwitterAPIKeys import SECRET_KEY as SK
from TwitterAPIKeys import ACCESS_TOKEN as AT
from TwitterAPIKeys import SECRET_TOKEN as ST


#fetch request token for twitter.
#return type: void
def requestToken(auth_handler):
    try:
        redirect_url = auth_handler.get_authorization_url()
    except:
        print ("Error! Failed to get request token.")
        exit()


'''
returns a list of a bunch of random tweets#
made by one specific user 
paramaters:
    string username(twitter username)
    string start(beginning time range to grab tweet from)
    string end(ending time range to grab tweet from)
    int count(the amount of tweets you want to grab)
return type: list[] (of tweets)    
'''
def getUserTweets(username, start, end, number_of_tweets):
    user = api.get_user(username)
    tweets = api.user_timeline(screen_name = username, count = user.statuses_count, include_rts = True)
    list_of_tweets = []

    i = 0
    while i < number_of_tweets:
        random_tweet = random.choice(tweets)
        if (random_tweet in list_of_tweets) or (date(random_tweet.created_at) < start) or (date(random_tweet.created_at) > end):
            i -= 1
        else:
            list_of_tweets.append(random_tweet.text)
            i += 1
    return list_of_tweets

#connect to the tweepy api
auth = tweepy.OAuthHandler(CK, SK)
auth.set_access_token(AT, ST)
#auth = tweepy.API(auth)
requestToken(auth)
api = tweepy.API(auth)


start = datetime.date(2016, 12, 31)
end = datetime.date(2018, 12, 31)
#getUserTweets("realdonaldtrump", start, end, 100)