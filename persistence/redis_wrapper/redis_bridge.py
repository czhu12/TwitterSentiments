import redis

class RedisBridge:
  def __init__(self, host="localhost", port=6379, db=0):
    self.redis = redis.StrictRedis(host=host, port=port, db=db)

  def addToken(self, key, value=1):
    #print 'Saving key ' + key + '\n'
    if(self.rContains(key)):
      self.rIncrement(key)
    else:
      self.rAdd(key, value)

  def rContains(self, key):
    return self.redis.get(key) is not None

  def rIncrement(self, key):
    self.redis.incr(key, amount=1)

  def rGet(self, key):
    return self.redis.get(key)

  def addAll(self, keys):
    for key in keys:
      self.addToken(key)

  def rAdd(self, key, value):
    self.redis.set(key, value)

  def clear(self):
    self.redis.flushall()

