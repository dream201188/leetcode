#
# @lc app=leetcode.cn id=125 lang=python
#
# [125] 验证回文串
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        length = len(s)
        i, j = 0, length - 1
        s = s.lower()
        while i < j:
            while i < length and not s[i].isalnum():
                i += 1
            while j > -1 and not s[j].isalnum():
                j -= 1

            if -1 < i < j < length:
                if  s[i] != s[j]:
                    return False
                else:
                    i, j = i + 1, j - 1
        return True
# @lc code=end

