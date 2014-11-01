class TweetParser:
  def __init__(self, stopWordsHandle):
    self.stopWordsHandle = stopWordsHandle
    self.initSet()
  
  def parse(self, text):
    text = text.lower()
    return " ".join(filter(lambda x: x not in self.stopWordsSet, text.split()))

  def initSet(self):
    setIt = []
    for word in self.stopWordsHandle:
      setIt.append(word[:-1])

    self.stopWordsSet = set(setIt)
      
  def removeStopWords(self, text):
    text = text.lower()
    return " ".join(filter(lambda x: x not in self.stopWordsSet, text.split()))
