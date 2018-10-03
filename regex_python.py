'''
\s      [ \n\t\f\r]
\S      [^ \n\t\f\r]
\w      [A-Za-z0-9_]
\d      [0-9]
\D      [^0-9]
\W      [^A-Za-z0-9_]
\b      word boundary
^       beginning of string
$       end of string
re.findall(pattern, string)
re.finditer(pattern, string)
re.search(pattern, string)
Hints:
    * patterns should raw strings r''
    * always start with findall() and move to search()
    * start with a small pattern and build-up one step at a time
'''
import re
from collections import Counter
from pprint import pprint

with open('notes/hamlet.txt') as f:
    play = f.read()
    
words = re.findall(r"[a-z\'\-]{3,}", play.lower())
pprint(Counter(words).most_common(50))
