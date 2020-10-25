#
# @lc app=leetcode.cn id=455 lang=python
#
# [455] 分发饼干
#


# @lc code=start
class Solution(object):

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        res, a, b = 0, 0, 0
        while a < len(g) and b < len(s):
            if g[a] <= s[b]:
                res += 1
                a += 1
                b += 1
            else:
                b += 1
        return res


# @lc code=end
