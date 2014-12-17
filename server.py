import zmq
import json
import operator

from article_analyzer.sentence_analyzer import SentenceAnalyzer
from article_analyzer.default_ratio_calculator import DefaultRatioCalculator
from article_analyzer.sentence_parser import SentenceParser

port = "5556"

sentence_parser = SentenceParser()
def main():
  context = zmq.Context()
  socket = context.socket(zmq.REP)
  socket.bind("tcp://*:%s" % port)

  print "Starting ZeroMQ on port %s" % port
  calculator = DefaultRatioCalculator()
  sentenceAnalyzer = SentenceAnalyzer(calculator)

  print '==================='
  while True:
    # This is when I want to parse the input
    ratio_by_tokens = {}
    send_message = {}

    messages = socket.recv()
    messages = json.loads(messages)
    print messages
    message_tokens = parseMessages(messages["data"])
    sorted_tokens = sorted(message_tokens.items(), key=operator.itemgetter(1))

    #print sorted_tokens
    for message_token_freq in sorted_tokens:
      ratio_by_tokens[message_token_freq[0]] = sentenceAnalyzer.getRatio(
          message_token_freq[0], 
          message_token_freq[1]
      )

    ratios_sorted = sorted(ratio_by_tokens.items(), key=operator.itemgetter(1))
    print ratios_sorted
    
    data = json.dumps(ratios_sorted)
    send_message["data"] = data
    socket.send(send_message)
    print '==================='
    
def parseMessages(messages):
  # messages right now is an array.
  messages_joined = ' '.join(messages)
  message_tokens = sentence_parser.tokenizeSentence(messages_joined)
  return message_tokens

if __name__ == "__main__":
  main()
