from twython import Twython 
import time

CONSUMER_KEY = 'mt7glo83nN3IFWJUBKCTXyafE'
CONSUMER_SECRET = 'WdhRzKe8WUCAwP0ZQqCLUF4dl4wT1TQiE9dzlPd9mRsGQY4MTL'
ACCESS_KEY = '43574128-4URIhlV5uZXxKVb5oOA4fRy8EoFRL2vB4aBYX12LY'
ACCESS_SECRET = '1buQoKZMXBo7fGEpGRyHxfnBU2hIqqHjApiBGIWaSvS4e'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
for i in range(0, 16): 
    user_timeline = twitter.get_user_timeline(screen_name="santawclaus",count=350)
    for tweet in user_timeline:
        print tweet['text']
