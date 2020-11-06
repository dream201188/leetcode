class Solution:

    def numDecodings(self, s: str) -> int:
        size = len(s)
        if size == 0:
            return 0

        # dp[i]：以 s[i] 结尾的前缀字符串的解码个数

        # 分类讨论：
        # 1、s[i] != '0' 时，dp[i] = dp[i - 1]
        # 2、10 <= s[i - 1..i] <= 26 时，dp[i] += dp[i - 2]
        dp = [0 for _ in range(size)]

        if s[0] == '0':
            return 0
        dp[0] = 1
        for i in range(1, size):
            if s[i] != '0':
                dp[i] = dp[i - 1]

            num = 10 * ord(s[i - 1]) + ord(s[i]

            if 10 <= num <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[-1]

    def numDecodings(self, s):

        if not s or s[0] == '0': # 先把特殊情况搞定
            return 0

        size = len(s)
        dp = [0 for _ in range(size)]
        dp[0] = 1
        for i in range(1, size):
            if s[i] != '0':
                dp[i] = dp[i - 1]

            num = int(s[i - 1:i + 1]) # int('02') 也是2

            if 10 <= num <= 26:
                if i == 1: # 只有两位的特殊情况
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[-1]
