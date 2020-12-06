#
# @lc app=leetcode.cn id=58 lang=python
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_arr = s.split()
        return  len(str_arr[-1]) if str_arr else 0

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s) - 1, -1, -1):
            if ans == 0 and s[i] == ' ':
                continue
            if ans != 0 and ' ' == s[i]:
                return ans

            if ' ' != s[i]:
                ans += 1
        return ans



# @lc code=end

