class Solution:

    def numDecodings(self, s: str) -> int:
        size = len(s)
        if size == 0:
            return 0

        # dp[i]：以 s[i] 结尾的前缀字符串的解码个数

        # 分类讨论：
        # 1、s[i] != '0' 时，dp[i] = dp[i - 1]
        # 2、10 <= s[i - 1..i] <= 26 时，dp[i] += dp[i - 2]
        dp = [0 for _ in range(size)]

        if s[0] == '0':
            return 0
        dp[0] = 1
        for i in range(1, size):
            if s[i] != '0':
                dp[i] = dp[i - 1]

            num = 10 * (ord(s[i - 1]) - ord('0')) + (ord(s[i]) - ord('0'))

            if 10 <= num <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[-1]

    """
    123001123
    dp 默认是 0，单个是0或者跟前面凑成01 或者 30 的都不符合也就是dp【】= 0

    "1201234"
    dp[0]=1;dp[1]=2;dp[2]=0, dp[2]+=dp[0]=1  (因为单独0无解， 只能拼1,20);
    dp[3]=dp[2]=1(因为01拼不成 不能因为01 拼不成就跳出循环)

    但是上面的00 后面即使计算也是0
    """
    def numDecodings(self, s):

        if not s or s[0] == '0': # 先把特殊情况搞定
            return 0

        size = len(s)
        dp = [0 for _ in range(size)]
        dp[0] = 1
        for i in range(1, size):
            if s[i] != '0':
                dp[i] = dp[i - 1]

            num = int(s[i - 1:i + 1]) # int('02') 也是2

            if 10 <= num <= 26:
                if i == 1: # 只有两位的特殊情况
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[-1]
"""
dp[i]定义为前i个字符的解码方法总数，对应s[0],s[1]...,s[i-1]

先不考虑包含'0'的复杂的边界情况:
先把字符s[i-1]单独拎出来，此时前i个字符的解码方法总数由前i-1个字符的解码方法总数决定:dp[i]=dp[i-1]
再把s[i]和s[i-1]拼起来
- 如果拼合之后的数字合法（在1~26范围内），此时前i个字符的解码方法总数由前i-2个字符的解码方法总数决定:dp[i]=dp[i-1]+dp[i-2]；
- 如果拼合之后不合法，拼合后>26:dp[i]=dp[i-1]
再考虑包含'0'的复杂的边界情况:
当前位不为'0',前一位为'0' ：dp[i]=dp[i-1]
当前位为'0',且和前一位拼合后合法:此时前i个字符的解码方法总数由前i-2个字符的解码方法总数决定,且'0'不能单独拎出来:dp[i]=dp[i-1]+dp[i-2]
当前位为'0',且和前一位拼合后不合法：那就没法整了，拼也不是不拼也不是，那整个就不成立了：dp[i]=0

作者：juneychen
链接：https://leetcode-cn.com/problems/decode-ways/solution/lc91jie-ma-fang-fa-zong-shu-by-juneychen/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
