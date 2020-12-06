#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]

        i = 0
        while i < len(strs[0]):
            flag = True
            for one in strs:
                if i >= len(one) or one[i] != strs[0][i]:
                    flag = False
                    break

            if not flag:
                break
            i +=1
        return strs[0][:i]


    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]

        i = 0
        while i < len(strs[0]):
            for one in strs:
                if i >= len(one) or one[i] != strs[0][i]:
                    return strs[0][:i]
            i += 1

        return strs[0]

    """
    写法更加简洁明了
    """
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        first_length, num_count = len(strs[0]), len(strs)
        for i in range(first_length):
            if any(i >= len(one) or one[i] != strs[0][i] for one in strs): # any 搭配厉害了
                return strs[0][:i]
        return strs[0] # 中间没有跳出，说明正好第一个就是最短公共长度

# @lc code=end

