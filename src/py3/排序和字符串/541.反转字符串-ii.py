#
# @lc app=leetcode.cn id=541 lang=python
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not s or len(s) == 1:
            return s

        s = list(s)
        def reversed(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1; j -= 1

        p = 0
        while p < len(s):
            reversed(p, min(p + k -1, len(s) - 1))
            p += 2*k
        return "".join(s)

    """
    reversed 是python自带的，不用自己写；
    reversed 不是在原地进行改写，而是return出来；
    """
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not s or len(s) == 1:
            return s

        s = list(s)
        p = 0
        while p < len(s):
            s[p:p + k] = reversed(s[p:p + k])
            p += 2*k
        return "".join(s)

# @lc code=end

