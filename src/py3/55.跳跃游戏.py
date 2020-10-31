class Solution(object):
    """
    贪心，从前往后跳
    """

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_pos = 0  #可能跳的最远的距离
        end = len(nums) - 1
        for i, num in enumerate(nums):
            if i > max_pos:  # 当前位置已经比能跳的最远还靠后了，肯定跳不到了
                return False
            if i + num > max_pos:  # 这两行 与 用max效果一样，但是比max效率更高
                # 每一步找一个最远可能的位置
                max_pos = i + num
            # max_pos = max(i + num, max_pos)
            if max_pos >= end:  #当前可能跳的最远位置已经比end要大了，说明能跳出去了
                return True
        return True

    """
    贪心，从后往前跳，其实跟从前往后跳差不多想法
    """

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        length = len(nums)
        end = length - 1
        for i in range(length - 2, -1, -1):  #从倒数第二个看，挨个去end落在的位置，看看能不能落到第一个
            if i + nums[i] >= end:
                end = i
        if end == 0:
            return True
        return False
