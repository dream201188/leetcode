class Solution(object):
"""
车里等孩子随手一写，OK！
dp 转换公式与写都超级简单；
唯一难点是处理base情况，dp我在grid外面多了一行和一列，这样第一行第一列可以统一公式；
但是得搞成左上角的上与左是零，第一行除了前面两个是0 都应该是很大，这样才不会被选上；
第一列同理也是除了第一个第二个也要是最大；所以我把二维表格搞成了最大的，特殊的搞成0
"""
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 0
        dp[1][0] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
        return dp[-1][-1]


    """
    在上面基础上优化一下;牛逼一遍过！！！！！！！！！
    也是在base上有点技巧，岩哥技巧桑驰dp[0]在初始化时候就是第一行；
    第一排从第二个挨个加前面的，这样第一排dp搞到手；
    然后从第二行开始循环，每次先弄第一个就是加上前面的数；然后从第二个往右赶
    """

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [num for num in grid[0]]
        for j in range(1, n):
            dp[j] += dp[j - 1]

        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        return dp[-1]
