package java_sub;

class MaxSubArray_53 {
    public int maxSubArray(int[] nums) {

        int length = nums.length;
        if (null == nums || nums.length == 0)
            return 0;

        if (1 == length)
            return nums[0];

        int[] dp = new int[length];
        int result = nums[0];
        dp[0] = nums[0];
        for (int i = 1; i < length; i++) {
            dp[i] = Math.max((dp[i - 1] + nums[i]), nums[i]);
            result = Math.max(result, dp[i]);
        }
        return result;
    }

    public static void main(String[] args) {
        MaxSubArray_53 ss = new MaxSubArray_53();
        int[] nums = { 1, 2 };
        int res = ss.maxSubArray(nums);
        System.out.println(res);
    }
}