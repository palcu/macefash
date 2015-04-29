from urllib2 import urlopen
import re

with open('friendScraper.2', 'r') as f:
  text = f.read()
  patterns = [
      'facebook\.com\\\/([a-zA-Z0-9.]{3,40})\"',
      'facebook\.com\/([a-zA-Z0-9.]{3,40})\?'
      ]

  matches = []
  for i in range(0, len(patterns)):
    matches += [x for x in re.findall(patterns[i], text) if not 'php' in x]

  matches = sorted(list(set(matches)))

  for x in enumerate(matches):
    print "#%i: %s" % x
