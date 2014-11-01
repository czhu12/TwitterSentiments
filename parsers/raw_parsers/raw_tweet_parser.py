import time
import json
class RawTweetParser:
  def parse(self, raw_tweet):
    jsonTweet = json.loads(raw_tweet)
    text = jsonTweet['text']
    print text

    return text.encode()
