#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#


# @lc code=start
class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        def dfs(index, length, digits, res, key_map, cur):
            if length == index:
                res.append(cur)
                return
            for tmp in key_map.get(digits[index]):
                dfs(index + 1, length, digits, res, key_map, cur + tmp)

        res = []
        key_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
            "9": "wxyz"
        }

        if not digits:
            return res

        dfs(0, len(digits), digits, res, key_map, "")
        return res


# @lc code=end
