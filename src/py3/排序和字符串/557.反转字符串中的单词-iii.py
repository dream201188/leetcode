#
# @lc app=leetcode.cn id=557 lang=python
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list = s.strip().split()
        tmp = [one[::-1] for one in str_list]
        return ' '.join(tmp)

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list = s.strip().split()[::-1]
        return ' '.join(str_list)[::-1]


# @lc code=end

