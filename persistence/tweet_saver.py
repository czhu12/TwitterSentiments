import nltk
from filters.token_filters.punctuation_filter import PunctuationFilter
from filters.raw_filters.exists_filter import ExistsFilter
from parsers.raw_parsers.raw_tweet_parser import RawTweetParser
from filters.retweet_filter import RetweetFilter

from parsers.quotation_parser import QuotationParser

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
    self.tokenFilterStream = self.getTokenFilterStream()

  def notify(self, raw_tweet):
    try: 
      self.handleNotification(raw_tweet)
    except:
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
      if self.tokenFilterStream.filter(token):
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
    parseStream.addParser(QuotationParser())

    return parseStream
  
  def getTokenFilterStream(self):
    tokenFilterStream = FilterStream()
    tokenFilterStream.addFilter(PunctuationFilter(open('resources/punctuation_words.txt')))
    return tokenFilterStream
