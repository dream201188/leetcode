#
# @lc app=leetcode.cn id=344 lang=python
#
# [344] 反转字符串
#

# @lc code=start
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if not s or len(s) == 1:
            return

        i ,j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1; j -= 1



# @lc code=end

