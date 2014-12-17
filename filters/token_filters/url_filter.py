import re
class URLFilter:
  def __init__(self):
    self.prog = re.compile("co/")
    
  def filter(self, token):
    return not (self.prog.match(token))
