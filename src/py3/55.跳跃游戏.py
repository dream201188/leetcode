#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#


# @lc code=start
class Solution(object):
    # 从前往后跳
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_pos = 0
        end = len(nums) - 1
        for i, num in enumerate(nums):
            if i > max_pos:  # 前面最远的距离也到不了当前这个了
                return False
            if i + num > max_pos:  # 这两行 与 用max效果一样，但是比max效率更高
                max_pos = i + num
            # max_pos = max(i + num, max_pos)
            if max_pos >= end:
                return True
        return True


# @lc code=end
