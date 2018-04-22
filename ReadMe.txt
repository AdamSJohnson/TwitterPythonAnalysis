TwitterComands.py relies on a provided key file to be named TwitterAPIKeys.py
Formatted as such:
CONSUMER_KEY = {The provided Consumer Key} 
SECRET_KEY = {The Provided secret key}
ACCESS_TOKEN = {Your access token}
SECRET_TOKEN = {Your secret access token}

def requestToken(auth_handler):
    try:
        redirect_url = auth_handler.get_authorization_url()
    except:
        print("Error! Failed to get request token.")
        exit()

#connect to the tweepy api
auth = tweepy.OAuthHandler(CONSUMER_KEY, SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, SECRET_TOKEN)
requestToken(auth)
API = tweepy.API(auth)
