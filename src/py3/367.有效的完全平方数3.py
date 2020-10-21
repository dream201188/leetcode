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

        ans = num // 2

        while ans * ans > num:
            ans = (ans + num // ans) // 2

        return ans * ans == num


# @lc code=end
