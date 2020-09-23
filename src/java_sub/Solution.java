package java_sub;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[]{map.get(complement), i};
            } else {
                map.put(nums[i], i);
            }
        }
        return null;
    }

    public static void main(String[] args) {
        int[] nums = {3, 2, 7, 11, 6, 15};
        int target = 9;
        Solution solution = new Solution();
        int[] index = solution.twoSum(nums, target);
        System.out.println(index[0] + "," + index[1]);
    }

}


