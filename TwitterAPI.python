#
# Obtaining data from Twitter using the 'tweepy' package. In order to 
# obtain an API key, you will first need to create a (free) Twitter 
# account. Then go here: https://apps.twitter.com/app/new to create a new 
# 'application'. 
#

import tweepy
from datetime import datetime,date,time
import numpy as np
import matplotlib.pyplot as pp

# Replace with your authentication credentials.
consumer_key = 'Le4vWWBCc12ngnQnCm4J4Wdd'
consumer_secret = 'sL0MYn3IFbXAB3FzdV3pZSSdqbTi43HeVG9YHyW9qi19LD'
access_token = '6188752MTGa6ceKGLTV93G4SI16jw3aV0pv9KfX5r8Bs'
access_token_secret = 'z6maN9lV2QptnLbfAKrnOk26OBLhtz3CRmbJt'

# Establish connection to Twitter API.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#Accessing Donald trump Tweeter Feed
user = api.get_user('realDonaldTrump')
#user = api.get_user('ArvindKejriwal')

print (user.screen_name)
#Account Created on
print (user.created_at)
print (type((user.created_at)))
print ('\n')
#Status Object
recent_tweets = api.user_timeline('realDonaldTrump',count = 200)
#recent_tweets = api.user_timeline('ArvindKejriwal',count = 200)
print (recent_tweets[0].created_at)
print (type((recent_tweets[0].created_at)))
print (type(recent_tweets[0]))
print (len(recent_tweets))

#Making a temporary Datetime Object and Storing the First 200 tweets
d = date(2000, 7, 14)
t = time(12, 30)
temp = (datetime.combine(d, t))
no_tweets = []
count  = 0

min_id = recent_tweets[0].id
date_curr = recent_tweets[0].created_at
print (date_curr)
print ('\n')

for tweets in recent_tweets:
    if (tweets.created_at.date() == date_curr.date()):
        count = count + 1
    else:
        no_tweets.append(count)
        count = 0
        date_curr = tweets.created_at
        
    if (tweets.id < min_id):
        min_id = tweets.id
        temp = tweets.created_at

print (temp)
print (no_tweets)

#Calulating the Same and Storing the result in no_tweets List
#Maximum Reachable tweets 3200

for i in range(0,15):
    recent_tweets = api.user_timeline('realDonaldTrump',count = 200,max_id=min_id-1)
    #recent_tweets = api.user_timeline('ArvindKejriwal',count = 200,max_id=min_id-1)
    min_id = recent_tweets[0].id
    date_curr = recent_tweets[0].created_at
    #count = 0
    for tweets in recent_tweets:
        if (tweets.created_at.date() == date_curr.date()):
            count = count + 1
        else:
            no_tweets.append(count)
            count = 0
            date_curr = tweets.created_at
        if (tweets.id < min_id):
            min_id = tweets.id
            temp = tweets.created_at

no_tweets.append(count)
count = 0
    
length = (len(no_tweets))
print (length)
print (temp)

#Plotting the Received Graph
x = np.arange(1,length+1)
no_tweets.reverse()
no_tweets = np.array(no_tweets)
pp.plot(x,no_tweets)
pp.ylabel('No of Tweets')
pp.xlabel('No of Days from March 2016')
