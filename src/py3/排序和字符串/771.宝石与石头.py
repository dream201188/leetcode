#
# @lc app=leetcode.cn id=771 lang=python
#
# [771] 宝石与石头
#

# @lc code=start
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jset = set(J)
        return sum(s in jset for s in S)

# @lc code=end

