import json
import re

class ExistsFilter:
  # Filter to see if a tween is deleted or not, also, checks english.
  def filter(self, raw_tweet):
    jsonTweet = json.loads(raw_tweet)
    if 'delete' in jsonTweet or jsonTweet['lang'].encode('utf-8') != u'en':
      return False

    return True
