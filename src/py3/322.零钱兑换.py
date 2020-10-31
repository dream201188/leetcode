from functools import lar_cache


class Solution:
"""
深度遍历或者回溯或者暴力法或者穷举吧，反正就是冒泡方式的去寻找
"""
    def coinChange(self, coins, amount):
        memo = [None] * (amount + 1)

        def dfs(left):
            if left == 0:
                return 0
            if left < 0:
                return -1
            if memo[left] is not None:
                return memo[left]
            ans = float('inf')
            for coin in coins:
                tmp = dfs(left - coin)
                if tmp > 0 and tmp < ans:
                    ans = tmp + 1
            memo[left] = ans if ans != float('inf') else -1
            return memo[left]

        return dfs(amount)
"""
唯一改动用python自带的缓存函数减少部分代码量
"""
    def coinChange(self, coins, amount):

        @lru_cache(amount)
        def dfs(left):
            if left == 0:
                return 0
            if left < 0:
                return -1
            ans = float('inf')
            for coin in coins:
                tmp = dfs(left - coin)
                if tmp >= 0 and tmp + 1 < ans:
                    ans = tmp + 1
            return ans if ans != float('inf') else -1

        return dfs(amount)

"""
国际站上搜来的大神代码，确实比上面的要简单很多哦
"""
def coinChange(self, coins, amount):
        dp = [0] + [float('inf')] * amount
        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

"""
国际站上搜来的大神代码，确实比上面的要简单很多哦
比我自己的题解把for循环用一行代替，min的是一组可能值的数组
"""
    def coinChange(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]
"""
计算机解决问题其实没有任何奇技淫巧，它唯一的解决办法就是穷举，穷举所有可能性。算法设计无非就是先思考“如何穷举”，然后再追求“如何聪明地穷举”。

列出动态转移方程，就是在解决“如何穷举”的问题。之所以说它难，一是因为很多穷举需要递归实现，二是因为有的问题本身的解空间复杂，不那么容易穷举完整。

备忘录、DP table 就是在追求“如何聪明地穷举”。用空间换时间的思路，是降低时间复杂度的不二法门，除此之外，试问，还能玩出啥花活？

作者：labuladong
链接：https://leetcode-cn.com/problems/coin-change/solution/dong-tai-gui-hua-tao-lu-xiang-jie-by-wei-lai-bu-ke/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
