#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#


# @lc code=start
class Solution:

    def coinChange(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]


# @lc code=end
