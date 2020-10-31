class Solution(object):

    # 回溯算法，或者 说是属性深度遍历
    def climbStairs(self, n):

        def dfs(index, ans):
            if index > n:
                return ans
            if index == n:
                ans += 1
                return ans

            ans = dfs(index + 1, ans)
            ans = dfs(index + 2, ans)
            return ans

        ans = dfs(0, 0)
        return ans

    # 斐波那契的动态优化
    def climbStairs(self, n):
        if n < 3:
            return n
        a, b = 1, 2
        for i in range(3, n + 1):
            b, a = a + b, b
        return b


if __name__ == "__main__":
    solution = Solution()
    ans = solution.climbStairs(5)
    print(ans)
