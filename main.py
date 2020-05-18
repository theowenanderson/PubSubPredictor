from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

user = "PubSubs_on_sale"
tweets = query_tweets("yes!")

file = open("data.json", "w")
for tweet in tweets:


df = pd.DataFrame(t.__dict__ for t in tweets)
