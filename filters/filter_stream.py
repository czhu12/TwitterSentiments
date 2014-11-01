class FilterStream:
  def __init__(self):
    self.filters = []

  def addFilter(self, fil):
    self.filters.append(fil)

  def filter(self, text):
    result = True
    for i in range(0, len(self.filters)):
      fil = self.filters[i]
      result = result and fil.filter(text)

    return result
