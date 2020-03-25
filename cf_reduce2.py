# 输入 user  item  new_score
# 输出格式 itema itemb  itemaS*itembS
#         itemb itema  itembS*itemaS

# map2
# for line in sys.stdin:
#     u, i, s =line.strip().split('\t')
#     print "%s\t%s\t%s" % (u, i, s)

import sys



# for line in sys.stdin:
#     u, i, s = line.strip().split("\t")
#     print("%s\t%s\t%s" % (u, i, s))

tempUser = None
same_user_list = []

for line in sys.stdin:
    user, item, score = line.strip().split("\t")
    if not tempUser:
        tempUser = user
    if user != tempUser:
        for i in range(0, len(same_user_list) - 1):
            for j in range(i + 1, len(same_user_list) - 1):
                itemA, scoreA = same_user_list[i]
                itemB, scoreB = same_user_list[j]
                print("%s\t%s\t%s" % (itemA, itemB, scoreA * scoreB))
                print("%s\t%s\t%s" % (itemB, itemA, scoreB * scoreA))

        same_user_list = []
        tempUser = user
    same_user_list.append((item, float(score)))

for i in range(0, len(same_user_list) - 1):
    for j in range(i + 1, len(same_user_list) - 1):
        itemA, scoreA = same_user_list[i]
        itemB, scoreB = same_user_list[j]
        print("%s\t%s\t%s" % (itemA, itemB, scoreA * scoreB))
        print("%s\t%s\t%s" % (itemB, itemA, scoreB * scoreA))

