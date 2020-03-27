# -*-coding:utf-8-*-

import sys

for line in sys.stdin:
    ss = line.strip().split(",")
    # ss=line.strip().split(',')
    if len(ss) != 3:
        continue
    u, i, s = ss
    print("%s\t%s\t%s" % (i, u, s))
