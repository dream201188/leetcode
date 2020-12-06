#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n, ans = len(matrix), len(matrix[0]), 0

        heights = [0] * n
        for i in range(m): # 把每一行换成了84题，得到一个ans后再比较大的那个是最后的解
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0

            left, right, stack = [0] * n, [n] * n, []
            for i, height in enumerate(heights):
                while stack and height < heights[stack[-1]]:
                    right[stack[-1]] = i
                    stack.pop()
                left[i] = stack[-1] if stack else -1
                stack.append(i)

            ans = max(ans, max([height * (right[i] - left[i] - 1) for i, height in enumerate(heights)]))
        return ans

"""
动态规划算法，时间复杂度更高，是上面算法的好几倍；
"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        maxarea = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0': continue

                width = dp[i][j] = dp[i][j - 1] + 1 if j > 0 else 1
                for k in range(i, -1, -1): # 从下到上看可能组成的矩形
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i - k + 1))
        return maxarea



# @lc code=end

