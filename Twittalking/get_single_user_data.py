import tweepy
import simplejson
from pprint import pprint

def getdata():
    consumer_key = 'Lhr5DVTV9rwM9WRi8EdX7uIeG'
    consumer_secret = 'RxTDeb1TmAP4Ys3WOzqDAkp9gZBb9my2jgQjpKARKE7sDbxrIZ'
    access_token = '937150765-o8pGcjJgWDof0zM7wayfmVcw1ijIVXLCEGz4Dvvx'
    access_token_secret = 'fU8qprEf0rq69s3H3GVafYdWxtgfnzBNHwMeXlqyAhiX1'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    # my_data = api.me()
    # print(simplejson.dumps(my_data._json, indent=4))

    user_data = api.get_user('andrecornaglia')
    return user_data

    # with open(file='twitterdata.txt', mode='a', encoding='utf-8') as file:
    #    file.write(str(user_data))
    #
    # return user_data

    # Pagination system return only 20 follower's data
    # user_followers = api.followers('candearabia')
    # for user in user_followers:
    #     print(simplejson.dumps(user._json, indent=4))

    # Cursor class takes care about pagination system
    # for user in tweepy.Cursor(api.followers, screen_name='screen_name_del_usuario').items(100):
    #     print(simplejson.dumps(user._json, indent=4))
    #
    # # Getting friends/followees
    # for user in tweepy.Cursor(api.friends, screen_name='screen_name_del_usuario').items(100):
    #     print(simplejson.dumps(user._json, indent=4))
    #
    # # Get an user timeline (all their tweets)
    # for tweet in tweepy.Cursor(api.user_timeline, screen_name='screen_name_del_usuario',
    #                            tweet_mode='extended').items(2):
    #     print(simplejson.dumps(tweet._json, indent=4))
    #
    # # Search for tweets
    # for tweet in tweepy.Cursor(api.search, q='Python', tweet_mode='extended'):
    #     print(simplejson.dumps(tweet._json, indent=4))

# if __name__ == '__main__':
#     sample = getdata()
#     pprint(sample, indent=4)