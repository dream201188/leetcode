class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if not nums or len(nums) < 4:
            return res
        length = len(nums)
        nums.sort()
        # 定义4个指针k，i，j，h  k从0开始遍历，i从k+1开始遍历，
        # 留下j和h，j指向i+1，h指向数组最大值
        for k in range(0, length - 3):
            # 当k的值与前面的值相等时忽略
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            # 第二层循环i，初始值指向k+1
            for i in range(k + 1, length - 2):
                # 当i的值与前面的值相等时忽略
                if i > k + 1 and nums[i] == nums[i - 1]:
                    continue
                # 定义指针j指向i + 1;
                # 定义指针h指向数组末尾
                j, h = i + 1, length - 1
                # 开始j指针和h指针的表演，计算当前和，如果等于目标值，j++并去重，h--并去重，
                # 当前和大于目标值时h--，当当前和小于目标值时j++
                while j < h:
                    curr = nums[k] + nums[i] + nums[j] + nums[h]
                    if curr == target:
                        res.append([nums[k], nums[i], nums[j], nums[h]])
                        j += 1
                        h -= 1
                        while j < h and nums[j] == nums[j - 1]:
                            j += 1
                        while j < h and nums[h] == nums[h + 1]:
                            h -= 1
                    elif curr > target:
                        h -= 1
                    else:
                        j += 1
        return res


        def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if not nums or len(nums) < 4:
            return res
        length = len(nums)
        nums.sort()
        # 定义4个指针k，i，j，h  k从0开始遍历，i从k+1开始遍历，
        # 留下j和h，j指向i+1，h指向数组最大值
        for k in range(0, length - 3):
            # 当k的值与前面的值相等时忽略
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            # 第二层循环i，初始值指向k+1
            for i in range(k + 1, length - 2):
                # 当i的值与前面的值相等时忽略
                if i > k + 1 and nums[i] == nums[i - 1]:
                    continue
                # 定义指针j指向i + 1;
                # 定义指针h指向数组末尾
                j, h = i + 1, length - 1
                # 开始j指针和h指针的表演，计算当前和，如果等于目标值，j++并去重，h--并去重，
                # 当前和大于目标值时h--，当当前和小于目标值时j++
                while j < h:
                    curr = nums[k] + nums[i] + nums[j] + nums[h]
                    if curr == target:
                        res.append([nums[k], nums[i], nums[j], nums[h]])
                        j += 1
                        h -= 1
                        while j < h and nums[j] == nums[j - 1]:
                            j += 1
                        while j < h and nums[h] == nums[h + 1]:
                            h -= 1
                    elif curr > target:
                        h -= 1
                    else:
                        j += 1
        return res
    """
    优化：判断不可能再组成四个数组和是target的时候，及时跳出循环；
    """
    def fourSum(self, nums, target):
        res = []
        if not nums or len(nums) < 4:
            return res
        length = len(nums)
        nums.sort()
        # 定义4个指针k，i，j，h  k从0开始遍历，i从k+1开始遍历，
        # 留下j和h，j指向i+1，h指向数组最大值
        for k in range(0, length - 3):
            # 当k的值与前面的值相等时忽略
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            """
            # 获取当前最小值，如果最小值比目标值大，说明后面越来越大的值根本没戏
            min1 = nums[k] + nums[k + 1] + nums[k + 2] + nums[k + 3]
            if min1 > target:
                break
            # 获取当前最大值，如果最大值比目标值小，说明后面越来越小的值根本没戏，忽略
            max1 = nums[k] + nums[length - 1] + nums[length - 2] + nums[length - 3]
            if max1 < target:
                continue
            """

            # 第二层循环i，初始值指向k+1
            for i in range(k + 1, length - 2):
                # 当i的值与前面的值相等时忽略
                if i > k + 1 and nums[i] == nums[i - 1]:
                    continue
                # 定义指针j指向i + 1;
                # 定义指针h指向数组末尾
                j, h = i + 1, length - 1

                """ # 获取当前最小值，如果最小值比目标值大，说明后面越来越大的值根本没戏
                min1 = nums[k] + nums[i] + nums[j] + nums[j + 1]
                if min1 > target:
                    break
                # 获取当前最大值，如果最大值比目标值小，说明后面越来越小的值根本没戏，忽略
                max1 = nums[k] + nums[i] + nums[h] + nums[h - 1]
                if max1 < target:
                    continue """

                # 开始j指针和h指针的表演，计算当前和，如果等于目标值，j++并去重，h--并去重，
                # 当前和大于目标值时h--，当当前和小于目标值时j++
                while j < h:
                    curr = nums[k] + nums[i] + nums[j] + nums[h]
                    if curr == target:
                        res.append([nums[k], nums[i], nums[j], nums[h]])
                        j += 1
                        h -= 1
                        while j < h and nums[j] == nums[j - 1]:
                            j += 1
                        while j < h and nums[h] == nums[h + 1]:
                            h -= 1
                    elif curr > target:
                        h -= 1
                    else:
                        j += 1
        return res

