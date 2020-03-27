# -*-coding:utf-8-*-


# 输入格式  itema itemb scorea*scoreb
# 经过map以后的输出格式 itema_itemb  scorea*scoreb
import sys

temp_key = None
score = 0.0

for line in sys.stdin:
    key, s = line.strip().split("\t")

    if not temp_key:
        temp_key = key
    if temp_key != key:

        ss = temp_key.split("SOH")
        if len(ss) != 2:
            continue
        item_a, item_b = ss
        print("%s\t%s\t%s" % (item_a, item_b, score))
        temp_key = key
        score = 0.0

    score += float(s)

ss = temp_key.strip().split("SOH")
if len(ss) != 2:
    sys.exit()
item_a, item_b = ss
print("%s\t%s\t%s" % (item_a, item_b, score))
