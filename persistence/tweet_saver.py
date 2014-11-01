import nltk
from filters.raw_filters.exists_filter import ExistsFilter
from parsers.raw_parsers.raw_tweet_parser import RawTweetParser
from filters.retweet_filter import RetweetFilter

from filters.filter_stream import FilterStream
from redis_wrapper.redis_bridge import RedisBridge
from parsers.parse_stream import ParseStream
from parsers.tweet_parser import TweetParser

class TweetSaver:
  def __init__(self):
    self.redisBridge = RedisBridge()
    self.rawFilterStream = self.getRawFilterStream()
    self.rawParseStream = self.getRawParseStream()
    self.parseStream = self.getParseStream()
    self.filterStream = self.getFilterStream()

  def notify(self, raw_tweet):
    print raw_tweet
    try: 
      self.handleNotification(raw_tweet)
    except UnicodeEncodeError:
      return

  def handleNotification(self, tweet):
    if self.rawFilterStream.filter(tweet):
      rawParseOut = self.rawParseStream.parse(tweet)
      if self.filterStream.filter(rawParseOut):
        parseOut = self.parseStream.parse(rawParseOut)
        self.save(parseOut)

  def save(self, parsedTweet):
    tokenized = nltk.word_tokenize(parsedTweet)
    for i in range(0, len(tokenized)):
      token = tokenized[i]
      self.redisBridge.addToken(token)

  def getRawFilterStream(self):
    rawFilterStream = FilterStream()
    rawFilterStream.addFilter(ExistsFilter())

    return rawFilterStream

  def getRawParseStream(self):
    rawParseStream = ParseStream()
    rawParseStream.addParser(RawTweetParser())

    return rawParseStream

  def getFilterStream(self):
    filterStream = FilterStream()
    filterStream.addFilter(RetweetFilter())

    return filterStream

  def getParseStream(self):
    parseStream = ParseStream()
    parseStream.addParser(TweetParser(open('resources/stopwords_formatted.1.txt')))

    return parseStream
