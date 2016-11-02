#Import the necessary methods from tweepy library
import tweepy
import json

#Variables that contains the user credentials to access Twitter API
access_token = "789624266954252288-2a8jGxOIZSitZcoDLrrHIZuwPWu2i5I"
access_token_secret = "6lkXgLKAKMFFqmP6QZEKcFCIvpTrREFczvYi3In9ob0GX"
consumer_key = "CJhL6wqb56Tj5U4AiBz8rWBLg"
consumer_secret = "DvCk0NFNJBEvogITwVuRM2iy4PUCIN6oEOOG1rVUuH2zZN6Iqu"
file = open("dataSample.txt", "a")

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        #decoded = json.loads(data)
        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        #print('@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))
        #print('')
        print(data)
        file.write(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print("Showing all new tweets for #programming:")

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this experiment follow #Halloween tag
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['#Halloween'])
