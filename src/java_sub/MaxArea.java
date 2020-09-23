package java_sub;

class MaxArea {
    public int maxArea(int[] height) {
        int maxArea = 0, left = 1, right = height.length - 1;

        while (left < right) {
            maxArea = Math.max((right - left) * Math.min(height[left], height[right]), maxArea);
            if (height[left] < height[right])
                left++;
            else
                right--;
        }
        return maxArea;
    }

    public static void main(String[] args) {
        int[] nums = { 1, 8, 6, 2, 5, 4, 3, 8, 7 };
        MaxArea solution = new MaxArea();
        int area = solution.maxArea(nums);
        System.out.println(area);
    }

}