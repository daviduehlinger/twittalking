import tweepy
import simplejson
import pprint


class TweetsListener(tweepy.StreamListener):

    def on_connect(self):
        print('Connected !!!')

    def on_status(self, status):
        # Save to DB
        print(status.text)

    def on_error(self, status_code):
        print('Ha ocurrido un error : ', status_code)


consumer_key = 'Lhr5DVTV9rwM9WRi8EdX7uIeG'
consumer_secret = 'RxTDeb1TmAP4Ys3WOzqDAkp9gZBb9my2jgQjpKARKE7sDbxrIZ'
access_token = '937150765-o8pGcjJgWDof0zM7wayfmVcw1ijIVXLCEGz4Dvvx'
access_token_secret = 'fU8qprEf0rq69s3H3GVafYdWxtgfnzBNHwMeXlqyAhiX1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

stream = TweetsListener()
streamingApi = tweepy.Stream(auth=api.auth, listener=stream)

# Filter
# follow recibe una lista con los ID de los usuarios
# track recibe una lista de palabras claves
# locations recibe un BoundingBox (coordenadas superior izquierda e inferior derecha de una zona geográfica)


streamingApi.filter(track=['coronavirus argentina'])

# search = api.search('Ginés Gonzalez García', lang='es', count=2)
# for tweet in search:
#     print(simplejson.dumps(tweet._json, indent=4))
