
def getTags():
  tags = []
  tag = raw_input("Enter a tag to search. Type [ENTER] to stop entering.\n")
  while(True):
    if tag == '':
      print "Finished entering tags."
      return tags

    tags.append(tag)
    tag = raw_input("Enter another tag.\n")

def main():
  tags = getTags()
  print tags


if __name__ == "__main__":
  main()
