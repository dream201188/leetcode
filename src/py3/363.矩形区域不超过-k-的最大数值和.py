"""
https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/javacong-bao-li-kai-shi-you-hua-pei-tu-pei-zhu-shi/
先通过方法3得到固定边界方案：

又通过https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/bao-li-onyou-hua-er-fen-er-fen-jian-zhi-by-lzh_yve/
理解了下面牛逼二分法

https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/gu-ding-zuo-you-bian-jie-qian-zhui-he-er-fen-by-po/
下面方法来自上面不过是提取成get_max
"""
"""
https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/qian-zhui-he-pai-xu-jin-ke-neng-tong-su-yi-dong-de/
在解这个问题前，我们先做另一道题：

给定一个长度为n的数组，求数组的最大子序和，这个子序和要求不能超过k。

首先，比如说[3, -1, 2, 4, -3, 2]，对于这个数组里我们假如取index为(2, 4)之间的子序列和（记为sum[2, 4]），即取[2, 4, -3]的和。而[2, 4, -3]的和其实会等于[3, -1, 2, 4, -3]的和减去[3, -1]的和。因此我们可以有这个结论：
sum[i, j] = sum[0, j] - sum[0, i - 1]。所以其实我们就是要求i和j，并且sum[i, j] <= k同时还得是最接近k的。

那么我们其实可以把问题转成，求sum[0, j] - sum[0, i - 1] <= k 同时保持最大。把这个式子变换一下就会是sum[0, j] - k <= sum[0, i - 1]

我们注意到sum[0, i - 1]会先计算出来，然后后面才计算出sum[0, j]。

这样的话我们可以把初始化一个cum，同时依次把数组的值加进去。每加一个，就把这个值丢到一个箱子里。并且每次把这个cum - k，并且在箱子里找到比cum - k大的值（这些值可能很多个，但我们只需要最小的那个）。为了查找方便，我们就把这个箱子维护成排序的箱子。

作者：capaldi
链接：https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/qian-zhui-he-pai-xu-jin-ke-neng-tong-su-yi-dong-de/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:

    def maxSumSubmatrix(self, matrix, k):
        row = len(matrix)
        col = len(matrix[0])
        res = float("-inf")
        for left in range(col):
            # 以left为左边界，每行的总和
            _sum = [0] * row
            for right in range(left, col):
                for j in range(row):
                    _sum[j] += matrix[j][right]
                res = self.get_max(_sum, k, res)
        return res

    # 看不懂这个二分法，反正很牛逼
    def get_max(self, _sum, k, res):
        # 在数组中求子序和最接近k的数
        import bisect
        arr = [0]
        cur = 0
        for tmp in _sum:
            cur += tmp
            # 二分法
            loc = bisect.bisect_left(arr, cur - k)
            if loc < len(arr):
                res = max(cur - arr[loc], res)
            bisect.insort(arr, cur)
        return res


"""
第三种方法优化
"""
class Solution:
  def maxSumSubarray(self, nums, k):
    # 排序的箱子
    array = [0]
    # 初始化cum
    cum = 0
    for num in nums:
      cum += num
      # 在array里找比cur - k大但最接近的数的位置
      # bisect_left是在array里返回比cur - k应该插入的位置
      loc = bisect.bisect_left(array, cur - k)
      # loc > len(arr)说明array里面的数都比cur - k小，代表没有找到值
      if loc < len(array):
        # 目前，对于每次遍历，cum - array[loc]都会是比k小的，但是我们不仅要比k小，我们还要最接近k，因此在这些数里面找最大
        res = max(cum - array[loc], res)
      # 记得把cum丢进箱子，并且还要维护排序
      bisect.insort(array, cur)
      return res

作者：capaldi
链接：https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/qian-zhui-he-pai-xu-jin-ke-neng-tong-su-yi-dong-de/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    import bisect
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        res = float('-inf')
        # 左边界
        for left in range(col):
            # 初始化nums（这个nums就是我们后面要用来求接近K的）
            nums = [0] * row
            # 右边界
            for right in range(left, col):
                for i in range(row):
                    nums[i] += matrix[i][right]
                # 在left, right为边界下的矩阵(在这里已经降维成1维的nums了)，
                # 下面这段求不超过k的最大数值和（跟前面我们讲的如出一辙）
                # 用来存cum的array（已排序）
                array = [0]
                cum = 0
                for num in nums:
                    cum += num
                    loc = bisect.bisect_left(array, cum - k)
                    if loc < len(array):
                        res = max(res, cum - array[loc])
                    bisect.insort(array

作者：capaldi
链接：https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/qian-zhui-he-pai-xu-jin-ke-neng-tong-su-yi-dong-de/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
