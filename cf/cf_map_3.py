# -*-coding:utf-8-*-

import sys

for line in sys.stdin:
    i_a, i_b, s = line.strip().split('\t')
    print("%s\t%s" % (i_a + "SOH" + i_b, s))
