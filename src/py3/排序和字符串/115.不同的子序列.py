#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)] # 上面一行1，左边一列0
        for j in range(n + 1):
            dp[0][j] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  + dp[i][j - 1] # 如果对应上要么选这个，那么个数跟左上角一样；要么不选这个字母就是左边
                else:
                    dp[i][j] = dp[i][j - 1]  # 如果长的那个不对应，只能看左边呗
        return dp[-1][-1]
# @lc code=end

