import nltk
from filters.filter_stream import FilterStream
from filters.token_filters.punctuation_filter import PunctuationFilter
from parsers.tweet_parser import TweetParser
from parsers.quotation_parser import QuotationParser
from parsers.parse_stream import ParseStream

class SentenceParser:
  def __init__(self):
    self.parseStream = self.getParseStream()
    self.tokenFilterStream = self.getTokenFilterStream()
    self.tokensCount = {}
    
  def getTokens(self):
    return self.tokensCount

  def tokenizeSentence(self, sentence):
    self.tokensCount = {}
    parseOut = self.parseStream.parse(sentence)
    self.tokenizeParse(parseOut)
    return self.getTokens()

  def tokenizeParse(self, parseOut):
    tokenized = nltk.word_tokenize(parseOut)
    for i in range(0, len(tokenized)):
      token = tokenized[i]
      if self.tokenFilterStream.filter(token):
        self.addToSet(token)

  def getParseStream(self):
    parseStream = ParseStream()
    parseStream.addParser(TweetParser(open('resources/stopwords_formatted.1.txt')))
    parseStream.addParser(QuotationParser())

    return parseStream

  def getTokenFilterStream(self):
    tokenFilterStream = FilterStream()
    tokenFilterStream.addFilter(PunctuationFilter(open('resources/punctuation_words.txt')))
    return tokenFilterStream

  def getTokenFilterStream(self):
    tokenFilterStream = FilterStream()
    tokenFilterStream.addFilter(PunctuationFilter(open('resources/punctuation_words.txt')))
    return tokenFilterStream

  def addToSet(self, token):
    if token in self.tokensCount:
      nextVal = self.tokensCount[token] + 1
      self.tokensCount[token] = nextVal
    else:
      self.tokensCount[token] = 1

