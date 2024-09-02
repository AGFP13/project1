import tweepy
import time
import datetime
import random
#import openpyxl
import requests
import os

def aleat():
    while True:
        alea=random.randrange(-10,10)
        print(alea)
        time.sleep(1)
#aleat()

api_key="MqMQjshYzQXd4XrvmTmjuUEOz"
api_key_secret="bpwyEG4Sn44iu0gFHuUJp6hvPFgpZiaoGb8RNhXqABhJSfs6R8"
bearer="AAAAAAAAAAAAAAAAAAAAAG0jowEAAAAAmAS9MO9dkobwQG%2Bm%2Fjw2HwtsoDg%3DeNsFqzDfVV2i8BmbeiuD9UXxwkY0zEagaIxunQr6h2OfV1Ts7K"
access_token="1501922448324927500-89N0XqwtQy9eVXQLBIqDLaKdvsZ9rr"
access_token_secret="Yz3oiLBMH0dJ7vgJjE3KtiY0xRZeyDzqi8FJvz5CuzP0w"

autherticator= tweepy.OAuthHandler(api_key, api_key_secret)
autherticator.set_access_token(access_token, access_token_secret)
api = tweepy.API(autherticator)

client = tweepy.Client(bearer)

def bordel(username):

        print(f"\n{datetime.datetime.now()}\n")
        #Moi = api.me()
        #print('Name: ' + Moi.name)
        user = api.get_user(screen_name=username)
        print(user.name)
        userDescription= dict(user._json)
        print(userDescription)
        print(user)
        time.sleep(15)

#bordel('LivePriceCrypto')

def tweet():
    print(f"\n{datetime.datetime.utcnow()}\n")
    #api.update_status("hello world-")

#tweet()

def test():
    from datetime import datetime

    # get current datetime
    dt = datetime.now()
    print('Datetime is:', dt)

    # get day of week as an integer
    x = dt.weekday()
    print('Day of a week is:', x)


#test()

def post():

    #tweets=api.search_tweets(q="#BTC", lang='en', count=100)

    tweets = client.search_recent_tweets(query='covid', max_results=100)

    for tweet in tweets.data:
        print(tweet.id)
post()