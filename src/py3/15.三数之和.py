from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if (nums is None) or (n < 3):
            return res

        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            l = i + 1
            r = n - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1

        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res

    """
    再刷一遍确实有收获
    """

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []
        length = len(nums)
        res = []
        nums.sort()
        for i in range(0, length - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, length - 1
            while j < k:
                """
                坑：[-2, 0, 0, 2, 2]
                1. 挨着的相同，那么需要跳过去，continue 跳出while 没用啊，后面还在继续走；
                2. while 光判断出来了，j k没有自己控制增长，相当于死循环了
                """
                # flag = False
                # while j < k and j > i + 1 and nums[j] == nums[j - 1]:
                #     j += 1
                #     flag = True
                # if flag:
                #     continue
                # while j < k < length - 1 and nums[k] == nums[k + 1]:
                #     k -= 1
                #     flag = True
                # if flag:
                #     continue

                cur = nums[i] + nums[j] + nums[k]
                if cur == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    """
                    这两个循环相当于上面的两个，比上面简单点，上面是一进来就检查是不是和最近经历的相同，相同就跳过
                    这两个循环是只有在已经找到答案的情况下判断是不是跟未来的下一个相同，从而去自增自减
                    """
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    k -= 1
                    j += 1
                elif cur > 0:
                    k -= 1
                else:
                    j += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([1, -1, -1, 0]))
