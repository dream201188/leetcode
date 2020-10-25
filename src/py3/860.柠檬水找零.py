#
# @lc app=leetcode.cn id=860 lang=python
#
# [860] 柠檬水找零
#


# @lc code=start
class Solution(object):

    def lemonadeChange(self, bills):
        if not bills:
            return False
        length = len(bills)
        q = []
        for i in range(length):
            if bills[i] > 5:
                if not q:
                    return False

                tmp = bills[i] - 5
                q.sort(reverse=True)
                for j in q[:]:  # for in 循环删除后出现问题， 要么改成while 自己控制i要么改成每次用q的副本
                    if tmp - j == 0:
                        tmp = tmp - j
                        q.remove(j)
                        break
                    elif tmp - j > 0:
                        tmp = tmp - j
                        q.remove(j)
                    else:
                        continue
                if tmp > 0:
                    return False
            q.append(bills[i])
        return True


# @lc code=end
