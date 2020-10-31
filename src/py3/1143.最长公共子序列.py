class Solution(object):

    # 动态规划算法：
    #dp 辅助的空间是（n+1）*（m+1）
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if not text1 or not text2:
            return 0

        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        print(dp[-1][-1])
        return dp[-1][-1]

    # 优化成一维数组，空间复杂度进一步降级成min（m,n)
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if not text1 or not text2:
            return 0

        m, n = len(text1), len(text2)
        if m < n:
            m, n = n, m
            text1, text2 = text2, text1
        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            pre = 0  # 每一行左上角从dp[0]开始也就是从0开始，之前放到循环外面了
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    pre, dp[j] = dp[j], pre + 1  # 保留pre和使用同时进行
                else:
                    pre, dp[j] = dp[j], max(dp[j], dp[j - 1])
        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    solution.longestCommonSubsequence("abcba", "abcbcba")
