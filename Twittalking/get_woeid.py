import time, uuid, urllib.request
import hmac, hashlib
from base64 import b64encode
import simplejson

"""
Basic info
"""
app_id = '1iwjOr74'
consumer_key = 'dj0yJmk9QlByUXZXTWFaMWxNJmQ9WVdrOU1XbDNhazl5TnpRbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTAx'
consumer_secret = 'ddbe645c629a0099229b3e226d3bc46285bf5794'
url = 'https://weather-ydn-yql.media.yahoo.com/forecastrss'
method = 'GET'
concat = '&'
query = {'location': 'córdoba,ar', 'format': 'json', 'u': 'c'}
oauth = {
    'oauth_consumer_key': consumer_key,
    'oauth_nonce': uuid.uuid4().hex,
    'oauth_signature_method': 'HMAC-SHA1',
    'oauth_timestamp': str(int(time.time())),
    'oauth_version': '1.0'
}

#Prepare signature string (merge all params and SORT them)

merged_params = query.copy()
merged_params.update(oauth)
sorted_params = [k + '=' + urllib.parse.quote(merged_params[k], safe='') for k in sorted(merged_params.keys())]
signature_base_str = method + concat + urllib.parse.quote(url, safe='') + concat + urllib.parse.quote(concat.join(sorted_params), safe='')

#Generate signature

composite_key = urllib.parse.quote(consumer_secret, safe='') + concat
oauth_signature = b64encode(hmac.new(composite_key.encode('utf-8'), signature_base_str.encode('utf-8'), hashlib.sha1).digest())

#Prepare Authorization header

oauth['oauth_signature'] = oauth_signature.decode('utf-8')
auth_header = 'OAuth ' + ', '.join(['{}="{}"'.format(k,v) for k,v in oauth.items()])

#Send request

url = url + '?' + urllib.parse.urlencode(query)
request = urllib.request.Request(url)
request.headers['Authorization'] = auth_header
request.headers['X-Yahoo-App-Id']= app_id
response = urllib.request.urlopen(request).read()

r = simplejson.loads(response.decode('utf-8'))

print('Location : ' + r['location']['city'])
print('Country : ' + r['location']['country'])
print('WOEID : ' + str(r['location']['woeid']))
