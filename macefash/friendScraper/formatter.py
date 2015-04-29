import sys
import re

v = []
for line in sys.stdin:
  s = line[:-2]

  pattern = r'facebook.com/(.+)'
  match = re.findall(pattern, s)[0]

  if '=' in match:
    match = re.findall(r'=(.+)', match)[0]

  v.append(match)

v = sorted(list(set(v)))

print '\n'.join(v)

