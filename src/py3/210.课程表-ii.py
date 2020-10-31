#
# @lc app=leetcode.cn id=210 lang=python
#
# [210] 课程表 II
#

# @lc code=start
import collections
"""
图的深度遍历的应用，主要学习到python三点
1. python3 里面有nonlocal关键字，python2 里面没有，所以要搞值传递，然后还要返回进行赋值；
2. 关于list的初始化
3. 每个课程是从0 到 n-1；所以数组可以看成是特殊的dict，index是key；也不需要顶点的
"""


class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        if not numCourses and not prerequisites:  #不用判断这个极端情况
            return []

        # edges = [[]] * numCourses    这样的话里面的list用同一个地址
        # edges = [[] for i in range(numCourses)]  这样的话是不同的新的list
        edges = collections.defaultdict(list)
        visitted = [0] * numCourses
        res = []
        valid = True  # python2 里面没有nonlocal，所以函数里只是值传递，所以要return出来

        for tmp in prerequisites:
            edges[tmp[1]].append(tmp[0])

        def dfs(index, valid):
            if not valid:
                return False

            visitted[index] = 1

            for course in edges[index]:
                if not valid:
                    return False
                if visitted[course] == 0:
                    valid = dfs(course, valid)

                if visitted[course] == 1:
                    valid = False
                    return valid

            visitted[index] = 2
            res.append(index)
            return True

        for course in range(numCourses):
            if valid and visitted[course] == 0:
                valid = dfs(course, valid)

        if not valid:
            return []

        return res[::-1]


if __name__ == "__main__":
    solution = Solution()
    solution.findOrder(1, [])

# @lc code=end
