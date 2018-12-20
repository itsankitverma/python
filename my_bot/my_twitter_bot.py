import tweepy
import time

print("this is my twitter bot")

CONSUMER_KEY = 'OEICFupJKcv2OVLt9NrmRnGGq'
CONSUMER_SECRET = '90h5s7ZBHrxPoBBTZzWDRwXOWOGhDx2NOtCgqSWUQdG7Ea2AwL'
ACCESS_KEY = '1073442806453002240-EG8orqHC62gTtDXx7ThBapZkyJ3MSQ'
ACCESS_SECRET = 'EWnmpMZVmqakAvJBqRouXaV5z2lfx7sNCM4xvQ1eFHc18'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print("retrieving and replying to tweets..")
 # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)


    mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + " -- " + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#heyankit' in mention.full_text.lower():
            print("Found #heyankit ")
            print("responding back...")
            api.update_status('@' + mention.user.screen_name + '#heyankit back to you!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(10)