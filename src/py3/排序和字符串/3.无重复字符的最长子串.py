#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        i, j, ans, length, pre_set = 0, 0, 0, len(s), set(s[0])
        for i in range(length):
            while j + 1 < length and s[j + 1] not in pre_set:
                pre_set.add(s[j + 1])
                j += 1
            ans = max(ans, j - i  + 1)
            pre_set.remove(s[i])
        return ans

# @lc code=end

