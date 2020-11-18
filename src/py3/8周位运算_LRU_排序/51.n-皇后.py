class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def dfs(path,cols, pie, na):
            row = len(path)
            if row == n:
                result.append(path)
                return

            availablePositions = ((1 << n) - 1) & (~(cols | na | pie)) # pie na 三个数1 表示皇后位置，取反后1表示可以放的位置
            while availablePositions:
                position = availablePositions & (-availablePositions) #获取最后一个1；
                availablePositions = availablePositions & (availablePositions - 1) # 将最后一个1变成0
                col_index = bin(position - 1).count("1")
                dfs(path + [col_index], cols | position, (pie | position) >> 1, (na | position) << 1)

        path,result = [], []
        dfs(path, 0, 0, 0)
        return [['.' * col + 'Q' + '.' * (n - col - 1) for col in path] for path in result]
if __name__ == "__main__":
    s = Solution()
    s.solveNQueens(4)

