class Solution(object):
"""
贪心算法：每一跳都选能选最的那个位置，巧妙的是不用去排序中间最大值，就挨个选；用最大值当边界；
"""
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        ans, end, max_pos = 0, 0, 0
        for i in range(length - 1):
            max_pos = max(i + nums[i], max_pos)
            if i == end:
                ans += 1
                end = max_pos
        return ans
