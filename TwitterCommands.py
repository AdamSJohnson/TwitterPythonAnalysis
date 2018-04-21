
#API setup and import
from TwitterAPIKeys import CONSUMER_KEY as CK
from TwitterAPIKeys import SECRET_KEY as SK
from TwitterAPIKeys import ACCESS_TOKEN as AT
from TwitterAPIKeys import SECRET_TOKEN as ST


import twitter
api = twitter.Api(consumer_key=CK,
                  consumer_secret=SK,
                  access_token_key=AT,
                  access_token_secret=ST)

from enum import Enum     

#Month enum for quick comparison
class Month(Enum):
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12

#We will first define a function to search based on the user handle
#The option for a start and end date should be availble 
def user_search(user='',start=None,end=None):
    #This method relies on getting a user name
    if(user==''):
        return 0
    #convert name to ID
    user_id = api.GetUser(screen_name=user).id
    
    #grab the statuses
    statuses = api.GetUserTimeline(user_id=user_id, count=100)
    #print(statuses)
    
    #This method should just return the text from the statuses
    ret = []
    for s in statuses:
        ret.append(s.text)
        #print(s)
        print((s.created_at))
    #interesting the created at parsing can be done like:
    # Mon Apr 16 23:42:42 +0000 2018
    # <day_of_week> <Month> <day> <time_24_hr_fmt> <offset> <year>
    return ret

def date_comp(date1='', date2=''):
    #if either date is empty just return 0
    if date1=='' or date2=='':
        return 0

    a = date1.replace('\n', '').split(' ')
    b = date2.replace('\n', '').split(' ')
    
    #moving forward the comparison will determine if a < b, a = b or a > b
    #compare year first only move on if a.year == b.year
    if int()
    return 0


if __name__ == '__main__':
    #user_search(user='BobJohnson93')
    date_comp(date1='Wed Apr 18 12:30:18 +0000 2018',
              date2='Mon Feb 19 14:22:05 +0000 2018')