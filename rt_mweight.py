import twitter, subprocess
from twitter.util import printNicely
'''
prequisites: install python and virtualenv

$ git clone git://github.com/kuenishi/mikanspweight
$ cd mikanspweight
$ virtualenv .
$ source bin/activate
$ unzip consumer.zip
$ python rt_mweight.py
...
Hi there! We're gonna get you all set up to use mikanspweight.

In the web browser window that opens please choose to Allow
access. Copy the PIN number that appears on the next page and paste or
type it here:



'''

def extract_consumer_data():
    filename = "consumer.zip"
    fp = open('consumer.txt')
    key = fp.readline().split(' ')[1].strip()
    secret = fp.readline().split(' ')[1].strip()
    fp.close()
    print(key)
    print(secret)
    return key, secret

def do_rt(authorization, id_str):
    t = twitter.Twitter(auth=authorization)
    return t.statuses.retweet(id=id_str)

def make_auth():
    key, secret = extract_consumer_data()
    oauth_token, oauth_token_secret = twitter.oauth_dance('mikanspweight',
                                                          key, secret)
    return twitter.OAuth(oauth_token, oauth_token_secret, key, secret)

if __name__ == '__main__':
    authorization = make_auth()
    stream = twitter.TwitterStream(auth = authorization,
                                   domain = 'userstream.twitter.com',
                                   api_version = '2')
    
    print('mikansp weight...')
    tweet_iter = stream.user()

    for tweet in tweet_iter:
        print('\nnew tweet!!! ============')
        if tweet.get('text'):
            #printNicely(tweet['text'])
            pass
        else:
            continue

        try:
            if u['screen_name'] == 'mikansp':
                if tweet['text'][:10] == 'My weight:':
                    r = do_rt(authorization, tweet['id_str'])
                    print("RT done:")
                    print(r)
                else:
                    print('@mikansp said: %s' % tweet['text'])
        except:
            continue
