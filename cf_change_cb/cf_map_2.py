# -*-coding:utf-8-*-

import sys

for line in sys.stdin:
    u, i, s = line.strip().split("\t")
    print("%s\t%s\t%s" % (u, i, s))
