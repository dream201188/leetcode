#
# @lc app=leetcode.cn id=51 lang=python
#
# [51] N 皇后
#
"""
内嵌函数的话，外层函数的变量是它的全局变量，好处是减少形参；
使用形参的话可以递归传值，而且用list合并相当于新的list传递，可以不必要reverse state
"""


# @lc code=start
class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def dfs(path, pie, na, result):
            row = len(path)
            if row == n:
                result.append(path)
                return None
            for col in range(n):
                if col not in path and col + row not in pie and row - col not in na:
                    dfs(path + [col], pie + [row + col], na + [row - col], result)

        result = []
        dfs([], [], [], result)
        return [['.' * col + 'Q' + '.' * (n - col - 1) for col in path] for path in result]


# @lc code=end
