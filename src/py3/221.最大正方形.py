class Solution(object):
    """
    dp(i,j) 表示以 (i, j)(i,j) 为右下角，且只包含 11 的正方形的边长最大值
    对于每个位置 (i, j)(i,j)，检查在矩阵中该位置的值：
    如果该位置的值是 00，则 dp(i, j) = 0dp(i,j)=0，因为当前位置不可能在由 11 组成的正方形中；
    如果该位置的值是 11，则 dp(i, j)dp(i,j) 的值由其上方、左方和左上方的三个相邻位置的 dpdp 值决定。具体而言，当前位置的元素值等于三个相邻位置的元素中的最小值加 11，状态转移方程如下：
    dp(i, j)=min(dp(i−1, j), dp(i−1, j−1), dp(i, j−1))+1
    """

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:  # 第一行与第一列比较特殊，如果是1，那么直接就是1，因为左上都没有
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    ans = max(ans, dp[i][j])
        return ans * ans

    """
    暴力法是最简单直观的做法，具体做法如下：
    遍历矩阵中的每个元素，每次遇到 11，则将该元素作为正方形的左上角；
    确定正方形的左上角后，根据左上角所在的行和列计算可能的最大正方形的边长（正方形的范围不能超出矩阵的行数和列数），在该边长范围内寻找只包含 11 的最大正方形；
    每次在下方新增一行以及在右方新增一列，判断新增的行和列是否满足所有元素都是 11。
    """

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        maxSide = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    maxSide = max(maxSide, 1)  # 当只有一个元素时候，下面for 进不去，最大边就是1，防止是0
                    kn_maxSide = min(rows - i, cols - j)
                    for k in range(1, kn_maxSide):
                        flag = True
                        if matrix[i + k][j + k] == '0':  # 可能的边长 1，2，3 ，先从小正方形对角线算起
                            break
                        for m in range(k):  #再一次算下面k行的 0，1，。。。k值，与右边k列的 0，1，2。。。k值
                            if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
                                flag = False
                                break
                        if flag:  #说明 k的情况下成立，如果不成立直接跳出
                            maxSide = max(maxSide, k + 1)
                        else:
                            break

        return maxSide * maxSide


if __name__ == "__main__":
    s = Solution()
    s.maximalSquare([["1"]])
