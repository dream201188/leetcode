class Solution:

"""
直接是动态转换方程，用动态规划方式求解
"""
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        dp = [0] * (length + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, length + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[-1]

"""
空间优化超级简单，实际上就是斐波那契数列的一样
"""
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        a = 0
        b = nums[0]
        for i in range(2, length + 1):
            b, a = max(b, a + nums[i - 1]), b
        return b
