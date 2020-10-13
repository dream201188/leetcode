#
# @lc app=leetcode.cn id=51 lang=python
#
# [51] N 皇后
#


# @lc code=start
class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        path, pie, na = [], [], []

        def dfs(row):
            if row == n:
                res.append(list(path))
                return
            for col in range(n):
                if col not in path and row + col not in pie and row - col not in na:
                    path.append(col)
                    pie.append(row + col)
                    na.append(row - col)
                    dfs(row + 1)
                    path.pop()
                    pie.pop()
                    na.pop()

        dfs(0)
        return [['.' * num + 'Q' + '.' * (n - num - 1) for num in path] for path in res]


# @lc code=end
