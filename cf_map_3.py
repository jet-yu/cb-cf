import sys

for line in sys.stdin:
    item_a, item_b, score = line.strip().split("\t")
    print("%s\t%s" % (item_a + "SOH" + item_b, score))
