#
# @lc app=leetcode.cn id=242 lang=python
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution(object):


    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        counter = {chr(97+i):0 for i in range(26)}
        for i in range(len(s)):
            counter[s[i]] += 1
            counter[t[i]] -= 1

        tmp = [False for i in range(26) if counter[chr(97+i)] != 0]
        return len(tmp) == 0

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        counter = {}
        for i in range(len(s)):
            counter[s[i]] = counter.setdefault(s[i], 0) + 1
            counter[t[i]] = counter.setdefault(t[i], 0) - 1

        tmp = [False for i in counter if counter[i] != 0]


        return len(tmp) == 0


    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        counter = {}
        for i in range(len(s)):
            counter[s[i]] = counter.setdefault(s[i], 0) + 1
            counter[t[i]] = counter.setdefault(t[i], 0) - 1

        return not any(counter[i] != 0 for i in counter)




# @lc code=end

