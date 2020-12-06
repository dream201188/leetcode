#
# @lc app=leetcode.cn id=818 lang=python3
#
# [818] 赛车
#

# @lc code=start
class Solution(object):
    def racecar(self, target: int) -> int:
        dp = [float('inf')] * (target + 1)

        for i in range(1, target + 1):
            k = 1 # A的次数
            pos = 1

            while pos < i:  # pos < target
                q = 0 # R过一次后A的次数
                while ((1 << q) - 1) < pos:
                    dp[i] = min(dp[i], k+1+q+1+dp[i-(pos-((1 << q) - 1))])
                    q += 1
                k += 1
                pos = (1 << k) - 1

            if i == pos: # pos == target
                dp[i] = k
            else: # pos > target
                dp[i] = min(dp[i], k + 1 + dp[pos-i])

        return dp[target]



class Solution(object):
    def racecar(self, target):
        dp = [0, 1, 4] + [float('inf')] * target
        for t in range(3, target + 1):
            k = t.bit_length()
            if t == 2 ** k - 1:
                dp[t] = k
                continue
            for j in range(k - 1):
                dp[t] = min(dp[t], dp[t - 2**(k - 1) + 2**j] + k - 1 + j + 2)
            if 2**k - 1 - t < t:
                dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)
        return dp[target]


# @lc code=end

