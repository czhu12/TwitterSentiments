import operator

from article_analyzer.article_parser import ArticleParser
from article_analyzer.article_analyzer import ArticleAnalyzer
from article_analyzer.default_ratio_calculator import DefaultRatioCalculator

def main():
  file_name = raw_input('Please enter name of file: \n')
  articleParser = ArticleParser(open('resources/example_articles/' + file_name))
  tokens = articleParser.getTokens()
  print tokens
  sortedTokens = sorted(tokens.items(), key=operator.itemgetter(1))
  calculator = DefaultRatioCalculator()
  articleAnalyzer = ArticleAnalyzer(calculator)

  ratiosByToken = {}
  for freqByToken in sortedTokens:
    try:
      ratiosByToken[freqByToken[0]] = articleAnalyzer.getRatio(freqByToken[0], freqByToken[1])
    except LookupError:
      continue

  ratiosSorted = sorted(ratiosByToken.items(), key=operator.itemgetter(1))
  print ratiosSorted

if __name__ == "__main__":
  main()

