import twitter_auth as auth
import oauth2 as oauth
import urllib2 as urllib

class TwitterStream:

  def __init__(self, auth_data = auth):
    self.oauth_token    = oauth.Token(key=auth_data.ACCESS_TOKEN, secret=auth_data.ACCESS_SECRET)
    self.oauth_consumer = oauth.Consumer(key=auth_data.CONSUMER_KEY, secret=auth_data.CONSUMER_SECRET)
    self.subscriptions = []

  def subscribe(self, callback):
    self.subscriptions.append(callback)

  def unsubscribe(self, callback):
    self.subscriptions.remove(callback)

  def fetchStream(self, parameters = []):
    url = "https://stream.twitter.com/1.1/statuses/sample.json"
    response = self.twitterReq(url, "GET", parameters)
    for line in response: 
      #print line
      for x in self.subscriptions:
        x.notify(line)

  def twitterReq(self, url, method, parameters):
    signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

    req = oauth.Request.from_consumer_and_token(self.oauth_consumer,
        token=self.oauth_token,
        http_method=method,
        http_url=url, 
        parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, self.oauth_consumer, self.oauth_token)

    if method == "POST":
      encoded_post_data = req.to_postdata()
    else:
      encoded_post_data = None
      url = req.to_url()

    opener = urllib.OpenerDirector()
    http_handler, https_handler = self.getHandlers()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    response = opener.open(url, encoded_post_data)

    return response


  def getHandlers(self):
    _debug=0
    http_handler  = urllib.HTTPHandler(debuglevel=_debug)
    https_handler = urllib.HTTPSHandler(debuglevel=_debug)
    return (http_handler, https_handler)
