import math
import sys
import xml.etree.ElementTree as et

file = sys.argv[1]
range_sep = "-"
rating_rep = ":"

def limit(s: str):
  [range_, rating] = s.split(rating_rep, 1)

  if range_sep in range_:
    [low, high] = map(int, range_.split(range_sep))

    range_ = range(low, high + 1)
  else:
    range_ = int(range_)
    range_ = range(range_, range_ + 1)

  return [range_, rating]

fragments = list(map(limit, sys.argv[2:]))
tree = et.parse(file)
myanimelist = tree.getroot()

for my_score in filter(lambda my_score: my_score.text != "0", myanimelist.iter("my_score")):
  score = int(my_score.text)

  if fragment := next(filter(lambda fragment: score in fragment[0], fragments), None):
    my_score.text = fragment[1]

tree.write("out.xml")
