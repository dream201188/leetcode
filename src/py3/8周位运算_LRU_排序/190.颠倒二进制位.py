#
# @lc app=leetcode.cn id=190 lang=python
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(31, -1, -1):
           ans += (n & 1) << i
           n >>= 1
        return ans

# @lc code=end

