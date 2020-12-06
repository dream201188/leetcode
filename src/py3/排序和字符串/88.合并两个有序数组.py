#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if not m:
            nums1[:] = nums2
            return

        nums1_copy = nums1[:m]
        # nums1[:] = []
        nums1 *= 0
        # nums1.clear()
        del nums1[:]
        ans = nums1
        nums1 = nums1_copy
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1

        while i < m:
            ans.append(nums1[i])
            i += 1

        while j < n:
            ans.append(nums2[j])
            j += 1

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if not m:
            nums1[:] = nums2
            return

        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >=0 and p2 >= 0:
            if nums1[p1] <= nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        nums1[:p2 + 1] = nums2[:p2 + 1]





# @lc code=end

