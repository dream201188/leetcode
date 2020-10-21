#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根
#


# @lc code=start
class Solution:

    def mySqrt(self, x):
        if x < 0:
            raise Exception('不能输入负数')
        if x == 0:
            return 0
        # 起始的时候在 1 ，这可以比较随意设置
        cur = 1.0
        while abs(cur * cur - x) > 1e-6:
            cur = (cur + x / cur) / 2
        return int(cur)


# @lc code=end
