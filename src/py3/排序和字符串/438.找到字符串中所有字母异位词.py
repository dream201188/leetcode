#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res, len_s, len_p = [], len(s), len(p)
        if len_p > len_s: return res
        comparator, temp_dict = [0] * 26, [0] * 26
        for i in range(len_p):
            comparator[ord(p[i])-ord('a')] += 1
            temp_dict[ord(s[i])-ord('a')] += 1
        for i in range(0, len_s-len_p+1):
            if temp_dict == comparator:
                res.append(i)
            if i + len_p < len_s:
                temp_dict[ord(s[i])-ord('a')] -= 1
                temp_dict[ord(s[i+len_p])-ord('a')] += 1
        return res


    def findAnagrams(self, s: str, p: str) -> List[int]:
        res, len_s, len_p = [], len(s), len(p)
        if len_p > len_s: return res
        p_list = list(p)
        p_list.sort()
        for i in range(0, len_s-len_p+1):
            tmp = list(s)[i:i + len_p]
            tmp.sort()
            if tmp == p_list:
                res.append(i)
        return res

# @lc code=end

