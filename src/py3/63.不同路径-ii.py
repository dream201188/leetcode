class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int

        空间复杂度 m*n
        dp[i][j] 含义是到右下角的路径数，一直从右下角推导到左上角
        """
        if not obstacleGrid or obstacleGrid[-1][-1] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for num in row] for row in obstacleGrid]
        dp[-1][-1] = 1
        """
        dp = [[0] * n] * m
        踩到了浅拷贝的坑，后面m个[0,0,0]相当于是复制的数组地址；
        声明采用上面的方式，每一行都新生成一个列表
        """

        # 最右边一列初始化，从倒第二个开始，自下向上，如果碰到1，就停止了，后面默认为0
        for i in range(m - 2, -1, -1):
            if obstacleGrid[i][n - 1] == 0:
                dp[i][n - 1] = 1
            else:
                break

        # 最下面一行，从倒数第二个开始，从右向左，如果碰到1就停止，后面默认也是0
        for j in range(n - 2, -1, -1):
            if obstacleGrid[m - 1][j] == 0:
                dp[m - 1][j] = 1
            else:
                break

        # 从倒数第二行，倒数第二列开始，先从右到左，再从下到上
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]

    # 空间复杂度变成一行
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[-1][-1] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0 for _ in range(n)]
        dp[-1] = 1  # 最后一个肯定是1，如果是0，直接就返回了

        for j in range(n - 2, -1, -1):  # 初始化最后一行，从倒数第二个从右往左进行
            # if obstacleGrid[m - 1][j] == 0:
            #     dp[j] = 1
            # else:
            #     break
            dp[j] = dp[j + 1] * (1 - obstacleGrid[m - 1][j])  # 相当于上面的if else 这样写更简洁

        # 从倒数第二行，倒数第二列开始，先从右到左，再从下到上
        for i in range(m - 2, -1, -1):
            dp[-1] = dp[-1] * (1 - obstacleGrid[i][-1])  #最右边列要特殊处理，因为它右边没有路径了
            for j in range(n - 2, -1, -1):
                # if obstacleGrid[i][j] == 0:
                #     dp[j] = dp[j] + dp[j + 1]
                # else:
                #     dp[j] = 0
                dp[j] = (dp[j] + dp[j + 1]) * (1 - obstacleGrid[i][j])  # 相当于上面的if else 这样写更简洁
        return dp[0]
