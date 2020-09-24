package java_sub;

import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=13 lang=java
 *
 * [13] 罗马数字转整数
 */

// @lc code=start
class Roma_13 {
    public int romanToInt(String s) {
        HashMap<String, Integer> map = new HashMap<>() {
            /**
             *
             */
            private static final long serialVersionUID = 1L;

            {
                put("I", 1);
                put("V", 5);
                put("X", 10);
                put("L", 50);
                put("C", 100);
                put("D", 500);
                put("M", 1000);
            }
        };

        int sum = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            int currentNum = map.get(s.substring(i, i + 1));
            int nextNum = map.get(s.substring(i + 1, i + 2));
            if (currentNum < nextNum)
                sum -= currentNum;
            if (currentNum >= nextNum)
                sum += currentNum;
        }
        sum += map.get(s.substring(s.length() - 1, s.length()));
        return sum;
    }

    public static void main(String[] args) {
        Roma_13 roma_13 = new Roma_13();
        int result = roma_13.romanToInt("XVII");
        System.out.println(result);

    }
}
