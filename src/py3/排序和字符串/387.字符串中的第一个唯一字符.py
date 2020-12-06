#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        counter = collections.Counter(s)
        for i,ch in enumerate(s):
            if counter[ch] == 1:
                return i
        return -1
# @lc code=end

