class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        tmp = n
        ans = 0
        while tmp: # 时间复杂度是 1 的个数
            tmp = tmp & (tmp - 1)
            ans += 1
        return ans

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        mask = 1
        ans = 0
        for i in range(1, 33):
            if (n & mask) != 0:
                ans += 1
            mask = mask << 1
        return ans

    def hammingWeight(self, n):
        res=0
        while n:   # 时间复杂度依赖最高为1 在哪
            res+=n&1
            n>>=1
        return res


if __name__ == "__main__":
    s = Solution()
    s.hammingWeight(0b00000000000000000000000000101011)

