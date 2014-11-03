import math
class DefaultRatioCalculator:
  def calculate(self, nativeFrequency, articleFrequency, term):
    #return nativeFrequency * math.log(1 + (1/articleFrequency))
    return nativeFrequency / articleFrequency

