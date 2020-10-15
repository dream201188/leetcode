#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#
"""
python用的是转成字符串，然后反转的方式输出；
我这用的是数学方式，是舍近求远，但是呢为了练习python基础
从这学到了 python的整除 取模 是负数的异常情况
比如 -7 // 4 是 -2
-7 % 4 是 1
"""


# @lc code=start
class Solution:

    def reverse(self, x):
        max = pow(2, 31) - 1
        min = pow(-2, 31)
        y = 0
        if x < 0:
            flag = -1
            x = x * flag
        while x:
            pop = x % 10
            if (y > max // 10) or (y == max // 10 and pop > 7):
                return 0
            if (y < min // 10) or (y == min // 10 and pop < -8):
                return 0
            y = y * 10 + pop
            x = x // 10
        print(y)
        return y * flag


# @lc code=end
