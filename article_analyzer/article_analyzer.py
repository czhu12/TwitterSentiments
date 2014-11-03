from persistence.redis_wrapper.redis_bridge import RedisBridge
class ArticleAnalyzer:
  def __init__(self, ratioCalculator):
    self.ratioCalculator = ratioCalculator
    self.redisBridge = RedisBridge()
   
  def getRatio(self, term, frequency):
    try:
      nativeFrequency = self.getNativeFrequency(term)
    except LookupError:
      raise LookupError

    if int(nativeFrequency) < 5:
      return 100000

    return self.ratioCalculator.calculate(float(nativeFrequency), float(frequency), term)

  def getNativeFrequency(self, term):
    if not self.redisBridge.rContains(term):
      raise LookupError

    return self.redisBridge.rGet(term)
