# 源数据格式  userid  itemid score
# 经过map1修改后的格式  itemid  userid  score 输出

# cf_reduce1.py 要做的是把map1输出的数据归一化
# 归一化 把同一个物品被不同用户打的打分平方 加起来开根号num，然后这个物品的被不用用户打的分除以num
# # 输出格式 userid  itemid  score/num
# item, userid, score = line.strip().split(' ') 这行需要修改' ' 实际是、t

import sys
import math

# map1
# for line in sys.stdin:
#     ss=line.strip().split('\t')
#     #ss=line.strip().split(',')
#     if len(ss) != 3:
#         continue
#     u, i, s = ss
#     print "%s\t%s\t%s" % (i, u, s)

for line in sys.stdin:
    ss = line.strip().split(",")
    if len(ss) != 3:
        continue
    u, i, s = ss
    print("%s\t%s\t%s" % (i, u, s))

current_item = None
same_item_list = []

for line in sys.stdin:
    item, userid, score = line.strip().split(' ')

    # 初始化 current_item 第一条数据只执行一次
    if not current_item:
        current_item = item

    if current_item != item:

        sum = 0.0
        for tuple in same_item_list:
            (u, s) = tuple
            sum += pow(s, 2)

        # 和开根号
        num = math.sqrt(sum)

        # 输出userid itemid new_score
        for tuple in same_item_list:
            (u, s) = tuple
            print("%s\t%s\t%s" % (userid, item, score / num))

        # 重置数据
        same_item_list = []
        current_item = item

    same_item_list.append((userid, score))

sum = 0.0
for tuple in same_item_list:
    (u, s) = tuple
    sum += pow(s, 2)

num = math.sqrt(sum)

for tuple in same_item_list:
    (u, s) = tuple
    print("%s\t%s\t%s" % (userid, item, score / num))
