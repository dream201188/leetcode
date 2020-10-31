from typing import List
"""
用了三种方法来实现
"""


class Solution:

    # 从上到下的深度遍历，找到一个结果后就算一个值，属于傻递归容易超时
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        ans, cur = 1e10, triangle[0][0]
        limit = len(triangle)

        def dfs(index, col):  # index 从1开始
            nonlocal ans
            nonlocal cur
            if index >= limit:  # terminator
                if cur < ans:
                    ans = cur
                return

            first = triangle[index][col]
            cur += first
            dfs(index + 1, col)
            cur -= first

            second = triangle[index][col + 1]
            cur += second
            dfs(index + 1, col + 1)
            cur -= second

        dfs(1, 0)
        print(ans)
        return ans

    # 计算在冒泡阶段进行计算，每个最小值都有，还可以记录下来；上面是属于下潜阶段结算
    # 最终结果就是最上面那个数和最小儿子的值进行相加
    # 其实所谓的动态规划就是从下往上的推上去
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        limit = len(triangle)
        cache = [[None] * len(row) for row in triangle]

        def dfs(index, col):
            if index == limit:  # terminator，到底后才开始计算
                return 0
            if cache[index][col] is not None:
                return cache[index][col]

            first = dfs(index + 1, col)
            second = dfs(index + 1, col + 1)
            cache[index][col] = min(first, second) + triangle[index][col]
            return cache[index][col]

        ans = dfs(0, 0)
        print(ans)
        return ans

    # 和上面唯一区别就是自己控制循环还是通过递归控制
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        m = len(triangle)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        # 从下往上推，由于下面数已经被保存过了，所以很自然的做了cashe
        for i in range(m - 1, -1, -1):
            for j in range(0, i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        return dp[0][0]

    # 将上面二维数组换成一维数组
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        m = len(triangle)
        dp = [0] * (m + 1)
        # 从下往上推，由于下面数已经被保存过了，所以很自然的做了cashe
        for i in range(m - 1, -1, -1):
            for j in range(0, i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]

    """
    总的来说其实这个还是很简单的关键是想明白，
    要从下往上算，求到最下的最短最大都从下往上算是好推理
    """

    # O(n*n/2) space, top-down
    def minimumTotal1(self, triangle):
        if not triangle:
            return
        res = [[0 for i in xrange(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    res[i][j] = res[i - 1][j - 1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i - 1][j - 1], res[i - 1][j]) + triangle[i][j]
        return min(res[-1])

    # Modify the original triangle, top-down
    def minimumTotal2(self, triangle):
        if not triangle:
            return
        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])

    # Modify the original triangle, bottom-up
    def minimumTotal3(self, triangle):
        if not triangle:
            return
        for i in xrange(len(triangle) - 2, -1, -1):
            for j in xrange(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]

    # bottom-up, O(n) space
    def minimumTotal(self, triangle):
        if not triangle:
            return
        res = triangle[-1]
        for i in xrange(len(triangle) - 2, -1, -1):
            for j in xrange(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]


if __name__ == "__main__":
    solution = Solution()
    solution.minimumTotal([[-1], [2, 3], [1, -1, -3]])
