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

        left, right = 2, num // 2

        while left <= right:
            mid = left + (right - left) // 2
            tmp = mid * mid
            if tmp == num:
                return True
            if tmp < num:
                left = mid + 1
            else:
                right = mid - 1

        return False


# @lc code=end
