import re
import sys

for line in sys.stdin:
    try:
        line = line.rstrip()
        if int(line, 2) % 3 == 0:
            print(line)
    except BaseException:
        pass