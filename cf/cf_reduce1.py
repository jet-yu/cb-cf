# -*-coding:utf-8-*-

# 源数据格式  userid  itemid score
# 经过map1修改后的格式  itemid  userid  score 输出

# cf_reduce1.py 要做的是把map1输出的数据归一化
# 归一化 把同一个物品被不同用户打的打分平方 加起来开根号num，然后这个物品的被不用用户打的分除以num
# # 输出格式 userid  itemid  score/num
# item, userid, score = line.strip().split(' ') 这行需要修改' ' 实际是、t

import sys
import math

current_item = None
same_item_list = []

for line in sys.stdin:
    item, user_id, score = line.strip().split('\t')

    if not current_item:
        current_item = item

    if current_item != item:

        sum = 0.0
        for tuple in same_item_list:
            (u, s) = tuple
            sum += pow(s, 2)

        num = math.sqrt(sum)

        for tuple in same_item_list:
            (u, s) = tuple
            print("%s\t%s\t%s" % (u, current_item, s / num))

        same_item_list = []
        current_item = item

    same_item_list.append((user_id, float(score)))

sum = 0.0
for tuple in same_item_list:
    (u, s) = tuple
    sum += pow(s, 2)

num = math.sqrt(sum)

for tuple in same_item_list:
    (u, s) = tuple
    print("%s\t%s\t%s" % (u, current_item, s / num))
