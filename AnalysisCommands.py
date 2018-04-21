from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

'''
    
    Status list analysis takes a list of text and runs
    sentiment analysis on each item in the list
    The return will be a list of scores.

'''
def status_list_analysis(statuslist=[]):
    #setup our intenisity analyzer
    sia = SentimentIntensityAnalyzer()
    scores = {}
    for status in statuslist:
        score = sia.polarity_scores(status)
        scores[status] = score
    print(scores)

def clean_status(status=''):
    #eventually we will clean this up
    return status

if __name__ == '__main__':
    sentences = [
        "VADER is smart, handsome, and funny.", # positive sentence example
    "VADER is smart, handsome, and funny!", # punctuation emphasis handled correctly (sentiment intensity adjusted)
    "VADER is very smart, handsome, and funny.",  # booster words handled correctly (sentiment intensity adjusted)
    "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
    "VADER is VERY SMART, handsome, and FUNNY!!!",# combination of signals - VADER appropriately adjusts intensity
    "VADER is VERY SMART, really handsome, and INCREDIBLY FUNNY!!!",# booster words & punctuation make this close to ceiling for score
    "The book was good.",         # positive sentence
    "The book was kind of good.", # qualified positive sentence is handled correctly (intensity adjusted)
    "The plot was good, but the characters are uncompelling and the dialog is not great.", # mixed negation sentence
    "A really bad, horrible book.",       # negative sentence with booster words
    "At least it isn't a horrible book.", # negated negative sentence with contraction
    ":) and :D",     # emoticons handled
    "",              # an empty string is correctly handled
    "Today sux",     #  negative slang handled
    "Today sux!",    #  negative slang with punctuation emphasis handled
    "Today SUX!",    #  negative slang with capitalization emphasis
    "Today kinda sux! But I'll get by, lol" # mixed sentiment example with slang and constrastive conjunction "but"
    ]
    
    status_list_analysis(statuslist=sentences)