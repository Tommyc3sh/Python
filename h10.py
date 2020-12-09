#christopher robin kaasik
#it20
import re

import re

fh = open('IP.txt')
for line in fh:
    if re.search('^[A-Z]+$', line):
         print(line,end='')







