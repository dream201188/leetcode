class Solution(object):
    """
    跟63比简直太简单了，在车里无聊随手写完；
    第二在第一上面优化一下空间复杂度；
    因为没障碍物也不是最优问题，所以直接mn的二维表格；
    第一行 第一列都是1，后面直接相加就好了；计算从第二行第二列直接走起
    后面的优化也没啥主意的因为第一个值必然已经跟上面相等了，也不需要进行特殊处理
    """
    """
    我故意的不同是从左上角往右下方推到：dp[i][j]意思是从开始到这i j有多少种路径；
    如果反方向的话应该是从ij到end有多少种方法
    """

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    def uniquePaths(self, m, n):
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]
        return dp[-1]
