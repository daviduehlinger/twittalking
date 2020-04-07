import tweepy

def get_followers_list():
    consumer_key = 'Lhr5DVTV9rwM9WRi8EdX7uIeG'
    consumer_secret = 'RxTDeb1TmAP4Ys3WOzqDAkp9gZBb9my2jgQjpKARKE7sDbxrIZ'
    access_token = '937150765-o8pGcjJgWDof0zM7wayfmVcw1ijIVXLCEGz4Dvvx'
    access_token_secret = 'fU8qprEf0rq69s3H3GVafYdWxtgfnzBNHwMeXlqyAhiX1'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    account_name = 'Python_MS_Fan'
    followers_list = []

    for individual in tweepy.Cursor(api.followers, screen_name=account_name).items(100):
        followers_list.append(individual._json)

    return followers_list