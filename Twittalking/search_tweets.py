import tweepy
import simplejson
import pprint


def search_tweets(words_to_search):
    consumer_key = 'Lhr5DVTV9rwM9WRi8EdX7uIeG'
    consumer_secret = 'RxTDeb1TmAP4Ys3WOzqDAkp9gZBb9my2jgQjpKARKE7sDbxrIZ'
    access_token = '937150765-o8pGcjJgWDof0zM7wayfmVcw1ijIVXLCEGz4Dvvx'
    access_token_secret = 'fU8qprEf0rq69s3H3GVafYdWxtgfnzBNHwMeXlqyAhiX1'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    query = ''.join(str(word) for word in words_to_search)
    searched_tweets = [status._json for status in tweepy.Cursor(api.search, q=query).items(1)]
    pprint.pp(searched_tweets)
    # Every tweet as json
    # for tweet in searched_tweets:
    #     print(tweet)
    #     pprint.pformat(tweet)
    return searched_tweets
