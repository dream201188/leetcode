class Solution(object):
    """
    桶思想：
    自己实现了Counter功能
    """

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # 获取出现次数dict
        nums = {}
        for task in tasks:
            nums[task] = nums.get(task, 0) + 1

        # 排序，获取最大次数
        sorted_nums = sorted(nums.items(), key=lambda x: x[1], reverse=True)
        max_count = sorted_nums[0][1]
        res = (max_count - 1) * (n + 1)
        # 找到最大次数个数
        for tmp in sorted_nums:
            if tmp[1] == max_count:
                res += 1
        # 比较tasks length
        res = res if res >= len(tasks) else len(tasks)
        return res

    """
    用counter 实现
    """

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter

        # 获取出现次数dict
        nums = Counter(tasks)
        # 排序，获取最大次数
        max_count = nums.most_common(1)[0][1]
        res = (max_count - 1) * (n + 1)
        # 找到最大次数个数
        # for tmp in nums.items():
        #     if tmp[1] == max_count:
        #         res += 1
        last_num = list(nums.values()).count(max_count)  # 等价
        res += last_num
        # 比较tasks length
        # res = res if res >= len(tasks) else len(tasks)]
        return max(res, len(tasks))  # 等价
        return res
