#
# @lc app=leetcode.cn id=917 lang=python
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """

        if not S or len(S) == 1:
            return S
        s = list(S)
        i ,j = 0, len(s) - 1
        while i < j:
            while i < len(s) and not (ord('a') <= ord(s[i]) <= ord('z') or ord('A') <= ord(s[i]) <= ord('Z')):
                i += 1
            while j > -1 and not (ord('a') <= ord(s[j]) <= ord('z') or ord('A') <= ord(s[j]) <= ord('Z')):
                j -= 1
            if -1 < i < j < len(s):
                s[i], s[j] = s[j], s[i]
                i += 1; j -= 1
        return ''.join(s)


    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """

        if not S or len(S) == 1:
            return S
        s = list(S)
        i ,j = 0, len(s) - 1
        while i < j:
            if not s[i].isalpha():
                i += 1
            if not s[j].isalpha():
                j -= 1
            if -1 < i < j < len(s) and s[i].isalpha() and s[j].isalpha():
                s[i], s[j] = s[j], s[i]
                i += 1; j -= 1
        return ''.join(s)


# @lc code=end

