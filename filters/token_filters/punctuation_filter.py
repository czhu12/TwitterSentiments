class PunctuationFilter:
  def __init__(self, punctuationHandle):
    self.punctuationHandle = punctuationHandle
    self.initSet()
    
  def initSet(self):
    setIt = []
    for word in self.punctuationHandle:
      setIt.append(word[:-1])

    self.punctuationWordsSet = set(setIt)

  def filter(self, token):
    return token not in self.punctuationWordsSet
