package java_sub;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class sum3_15 {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        int length = nums.length;
        if (null == nums || length < 3) {
            return res;
        }
        Arrays.sort(nums);
        for (int i = 0; i < length; i++) {
            if (nums[i] > 0) {
                return res;
            }

            if (i > 0 && nums[i - 1] == nums[i]) {
                continue;
            }
            int l = i + 1, r = length - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum == 0) {
                    res.add(new ArrayList<>(Arrays.asList(nums[i], nums[l], nums[r])));
                    while (l < r && nums[r - 1] == nums[r]) {
                        r--;
                    }
                    while (l < r && nums[l + 1] == nums[l]) {
                        l++;
                    }
                    l++;
                    r--;
                } else if (sum < 0) {
                    l++;
                } else {
                    r--;
                }
            }
        }

        return res;
    }
}
