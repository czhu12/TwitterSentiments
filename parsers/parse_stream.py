import nltk
class ParseStream:
  def __init__(self):
    self.parsers = []

  def addParser(self, parser):
    self.parsers.append(parser)

  def parse(self, input_string):
    result = input_string

    for i in range(0, len(self.parsers)):
      result = self.parsers[i].parse(result)

    return result
