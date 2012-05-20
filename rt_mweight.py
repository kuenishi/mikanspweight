import twitter, subprocess, datetime, sys
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

def do_rt(authorization, id_str, tw = None):
    t = None
    if tw is None:  t = twitter.Twitter(auth=authorization)
    else:           t = tw
    r = t.statuses.retweet(id=id_str)
    print(r)
    return t

def say(authorization, serif, tw = None):
    t = None
    if tw is None:  t = twitter.Twitter(auth=authorization)
    else:           t = tw
    r = t.statuses.update(status=serif)
    print(r)
    return t

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
        now = datetime.datetime.now().ctime()
        if tweet.get('text'): pass
        else:                 continue

        u = tweet['user']
        if u['screen_name'] == 'mikansp':
            print('\n@mikansp said: %s %s' % (tweet['text'], now))
            if tweet['text'][:10] == 'My weight:':
                t = do_rt(authorization, tweet['id_str'], tw=None)
                weight = float(tweet['text'][11:15])
                serif = "[mikansp forecast] %.1f kg. (%s)" % ((weight + 0.7), now)
                say(authorization, serif, tw=t)
                print("RT done: %s (%s)" % (weight, now))
        else:
            sys.stdout.write('.')
            sys.stdout.flush()
