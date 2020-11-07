class Solution:
    # 深度搜索，纯递归，也就是暴力递归
    def canCross(self, stones):
        length = len(stones)
        if stones[1] > 1:
            return False
        flag = False

        def dfs(level, k):
            nonlocal flag
            if flag or level == length - 1:
                flag = True
                return

            i = level
            cur_p = stones[i]
            for new_k in range(k + 1, k - 2, -1):
                new_p = cur_p + new_k
                if new_p in stones and stones[i] < new_p:
                    dfs(stones.index(new_p), new_k)

        dfs(1, 1)
        return flag

    """
    在上面基础上进行记忆化搜索
    """

    def canCross(self, stones: List[int]) -> bool:
        length = len(stones)
        if stones[1] > 1:
            return False
        from functools import lru_cache

        # 随便哪条路走到了，相同的 level k都可以
        # 同样的 level k走不到的 也不用再走 因为后面的路尝试了
        @lru_cache(None)
        def dfs(level, k):
            if level == length - 1:
                return True

            i = level
            cur_p = stones[i]
            for new_k in range(k + 1, k - 2, -1):
                new_p = cur_p + new_k
                if new_p in stones and stones[i] < new_p:
                    flag = dfs(stones.index(new_p), new_k)
                    if flag:
                        return True
            return False

        return dfs(1, 1)

    # dp[i][j] 表示上一步步数为j是否能到达i的位置
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[False] * n for _ in range(n)]
        dp[0][1] = True
        for i in range(1, n):
            for j in range(i):
                diff = stones[i] - stones[j]
                if diff >= n or not dp[j][diff]:
                    continue
                dp[i][diff] = True  # 凭实力上一步达到的位置；
                # 后面是为了方便下一步计算，表示k-1 k+1也行
                if diff - 1 >= 0:
                    dp[i][diff - 1] = True
                if diff + 1 < n:
                    dp[i][diff + 1] = True

        return any(dp[-1])
