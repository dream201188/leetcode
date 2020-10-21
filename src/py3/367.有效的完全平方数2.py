#
# @lc app=leetcode.cn id=367 lang=python
#
# [367] 有效的完全平方数
#


# @lc code=start
class Solution(object):

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True

        ans = 1.0

        while abs(ans * ans - num) > 1e-6:
            ans = (ans + num / ans) / 2

        ans = int(ans)
        if ans * ans == num:
            return True
        else:
            return False


# @lc code=end
