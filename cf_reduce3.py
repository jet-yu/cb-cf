# 输入格式  itema itemb scorea*scoreb
# 经过map以后的输出格式 itema_itemb  scorea*scoreb

# for line in sys.stdin:
#     i_a, i_b, s = line.strip().split('\t')
#     print "%s\t%s" % (i_a +"SOH"+i_b, s)

import sys

for line in sys.stdin:
    itema, itemb, score = line.strip().split("\t")
    print("%s\t%s" % (itema + "SOH" + itemb, score))

temp_key = None
sum = 0.0

for line in sys.stdin:
    key, score = line.strip().split("\t")

    if not temp_key:
        temp_key = key
    if temp_key != key:

        ss = key.strip().split("SOH")
        if len(ss) != 2:
            continue
        itema, itemb = ss
        print("%s\t%s\t%d" % (itema, itemb, sum))
        temp_key = key
        sum = 0.0

    sum += float(score)

ss = key.strip().split("SOH")
if len(ss) != 2:
    sys.exit()
itema, itemb = ss
print("%s\t%s\t%d" % (itema, itemb, sum))
