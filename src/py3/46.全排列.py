"""

"""


class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []
        length = len(nums)
        used = [False] * length

        def dfs(index, path):
            if index == length:
                # python 2 不允许直接修改父函数的变量 x ，其判断是否修改的依据是看 x 的id
                # res = res + [path]
                res.append(path)
                return
            for i, num in enumerate(nums):
                if not used[i]:
                    # path.append(num)
                    used[i] = True
                    dfs(index + 1, path + [num])  # 每次新生成一个path 所以res 可以直接append
                    # 如果改成回溯的办法，那相当于同一个地址，res append要改成 path[:]
                    # path.pop()
                    used[i] = False

        dfs(0, [])
        return res
