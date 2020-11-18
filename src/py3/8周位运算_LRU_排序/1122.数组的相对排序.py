#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution(object):
    """
    基数排序
    """
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        upper = max(arr1)
        frequency = [0] * (upper + 1)
        for x in arr1:
            frequency[x] += 1

        ans = list()
        for x in arr2:
            ans.extend([x] * frequency[x])
            frequency[x] = 0
        for x in range(upper + 1):
            if frequency[x] > 0:
                ans.extend([x] * frequency[x])
        return ans

    """
    完全自己实现版本，一遍AC，根据题意直接做
    """
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for value in arr2:
            num = arr1.count(value)
            res += [value] * num
            for i in range(num):
                arr1.remove(value)
        arr1.sort()
        res += arr1
        return res
    """
    利用python对元组的排序，arr2 按成一等级在前面，里面按照arr2的出现次数排序，其他按照大小排序
    """
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        rank = {value:i for i, value in enumerate(arr2)}
        arr1.sort(key=lambda value: (0, rank[value]) if value in rank else (1, value))
        return arr1



# @lc code=end

