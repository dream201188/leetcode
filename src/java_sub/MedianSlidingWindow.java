package java_sub;

import java.util.Arrays;

class MedianSlidingWindow {
    public double[] medianSlidingWindow(int[] nums, int k) {
        if (nums.length == 0) {
            return new double[0];
        }
        if (nums.length == 1) {
            return new double[] { nums[0] };
        }
        double[] res = new double[nums.length - k + 1];
        int cnt = 0;
        for (int i = 0; i <= nums.length - k; i++) {
            int[] cur = new int[k];
            for (int j = 0; j < k; j++) {
                cur[j] = nums[i + j];
            }
            Arrays.sort(cur);
            if (k % 2 == 0) {
                res[cnt++] = (cur[k / 2 - 1]) / 2.0 + cur[k / 2] / 2.0;
            } else {
                res[cnt++] = cur[k / 2];
            }
        }
        return res;
    }
}