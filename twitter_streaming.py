#Import the necessary methods from tweepy library
# import simplejson as json
# import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import time
# import json
import pandas

start = time.time()

file_out_name = "twitterdata.txt"

#Variables that contains the user credentials to access Twitter API 
access_token = "1054189340342059008-xiZK0Bc1hmjXcdOuIbql6BIIaKB4Hz"
access_token_secret = "C0OvikHAEH2mhEoRtQa0T8xqpVP6IDotCnVM3EISf5X2j"
consumer_key = "ayUjQpIob7F8FDULAOc5V062P"
consumer_secret = "RNxpkiFBin3QMr0vwnnrWVUbP6XVkmCHxB6ug4t5VvxAj47o61"

tweets = set()


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def __init__(self, api=None):
        super(StdOutListener, self).__init__()
        self.num_tweets = 0
        self.limit = 50

    def on_error(self, status):
        print status
        
    def on_status(self, status):
        # print('{"text":\"' + status.text.encode('utf-8') + '\"}') #See Tweepy documentation to learn how to access other fields
        tweets.add(status.text.encode('utf-8'))
        self.num_tweets += 1
        if self.num_tweets < self.limit:
            return True
        else:
            return False


def stream():
        #This handles Twitter authetification and the connection to Twitter Streaming API
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        # api = tweepy.API(auth,wait_on_rate_limit=True)
        # for tweet in tweepy.Cursor(api.search,q="bmw",count=2,lang="en", since="2019-01-03").items():
        #     tweets.add(tweet)



        stream = Stream(auth, l)

        # #This line filter Twitter Streams to capture data by the keywords
        stream.filter(track=['bmw', 'mercedes', 'lexus', 'audi'], languages=['en'])

        with open(file_out_name, 'w') as file:
            for tweet in tweets:
                file.write("{\"text\":\"%s\"}\n" % tweet)

        # time.sleep(runtime)
        # stream.disconnect()


if __name__ == '__main__':
    stream()
    print(str(len(tweets)) + " tweets in " + str(time.time() - start) + " seconds")

