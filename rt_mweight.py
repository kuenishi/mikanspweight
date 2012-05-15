import twitter, subprocess
'''
prequisites: install python and virtualenv

$ git clone git://github.com/kuenishi/mikanspweight
$ cd mikanspweight
$ virtualenv .
$ source bin/activate
$ python rt_mweight.py
username:
password:
...

'''

def extract_consumer_data():
    filename = "consumer.zip"
    #z = subprocess.call(['unzip', filename])
    fp = open('consumer.txt')
    key = fp.readline().split(' ')[1].strip()
    secret = fp.readline().split(' ')[1].strip()
    fp.close()
    print(key)
    print(secret)
    return key, secret

def run():
    key, secret = extract_consumer_data()
    oauth_token, oauth_token_secret = twitter.oauth_dance('mikanspweight', key, secret)
    t = twitter.Twitter(auth=twitter.OAuth(oauth_token, oauth_token_secret, key, secret))
    t.statuses.update(status='Hello, world!')

if __name__ == '__main__':
    run()
    print('mikansp weight...')
    

