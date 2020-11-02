class Solution(object):
    """
    遇到3个坑：
    1.排序后直接返回i j，跟期望顺序不一致；
    2.解决1，深度复制一个tmp，用值去查原表的index，又会碰到[3，3]的情况
    3.直接nums.remove(tmp[i])，再查出的tmp[j]在i后后面， index 会少1，所以我直接给赋值一个最大的
    """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if not nums:
            return []
        tmp = [num for num in nums]
        tmp.sort()
        i, j = 0, len(tmp) - 1
        while i < j:
            cur = tmp[i] + tmp[j]
            if cur == target:
                first = nums.index(tmp[i])
                nums[first] = float('inf')
                second = nums.index(tmp[j])
                return [first, second]
            if cur < target:
                i += 1
            if cur > target:
                j -= 1
        return []

    """
       一遍哈希
    """

    def twoSum(self, nums, target):
        if not nums:
            return []
        num_map = {}
        for i, num in enumerate(nums):  # 一遍循环前面的数进map
            if (target - num) in num_map:
                return [num_map[target - num], i]
            else:
                num_map[num] = i  # 即使后面有相同值，恰巧后面顶替了，不会用前面的
                # [2,2,7] 返回的是 1，2
        return []
