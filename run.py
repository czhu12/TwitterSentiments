from persistence.tweet_saver import TweetSaver
from twitter.twitter_stream import TwitterStream


def main():
  tweetSaver = TweetSaver()
  twitterStream = TwitterStream()
  twitterStream.subscribe(tweetSaver)
  #twitterStream.subscribe(NotifyTest())
  twitterStream.fetchStream()

class NotifyTest:
  def notify(self, text):
    print(text)

if __name__ == "__main__":
  main()
