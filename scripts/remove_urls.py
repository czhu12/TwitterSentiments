import redis
def main():
  redisBridge = RedisBridge()
  redisBridge.scanAll()

def scanRedis(data, redisHandle):
  print data
  for key in data:
    redisHandle.rDel(key)

if __name__ == "__main__":
  main()
