from typing import Union
from fastapi import FastAPI
import os
import tweepy

app = FastAPI()

client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_KEY_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
)
@app.get("/")
def read_root():
    return {"Hello": "World 3"}

@app.get("/tweets")
def get_tweets():
    print('abc')
    public_tweets = client.search_all_tweets("bolsonaro")
    for tweet in public_tweets:
        print(tweet.text)
    return {"Message": public_tweets}
