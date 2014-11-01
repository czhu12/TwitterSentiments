class QuotationParser:
  def parse(self, text):
    listPrevText = list(text)
    newListPrevText = []
    for char in listPrevText:
      if char == '"':
        continue

      if char == '.' or char == ',':
        newListPrevText.append(" ")
        continue

      newListPrevText.append(char)
    return ''.join(newListPrevText)
