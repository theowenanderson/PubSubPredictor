from twitterscraper import query_tweets
import pandas as pd

df2 = pd.read_json (r'/Users/owena/PubSubPredictor/tweets.json')
df1 = df2[df2['text'].str.contains("Yes!")] 
