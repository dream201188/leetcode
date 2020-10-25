#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#


# @lc code=start
class Solution(object):
    # 从前往后跳，其实跟从前往后跳差不多想法
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        length = len(nums)
        end = length - 1
        for i in range(length - 2, -1, -1):
            if i + nums[i] >= end:
                end = i
        if end == 0:
            return True
        return False


# @lc code=end
