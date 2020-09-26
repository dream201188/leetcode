package java_sub;
/*
 * @lc app=leetcode.cn id=5 lang=java
 *
 * [5] 最长回文子串
 */

// @lc code=start
class LongestPalindrome_5 {
    public String longestPalindrome(String s) {
        int length = s.length();
        boolean[][] dp = new boolean[length][length];
        String result = "";

        for (int l = 0; l < length; l++) {
            for (int i = 0; i + l < length; i++) {
                int j = i + l;
                if (l == 0) {
                    dp[i][i] = true;
                } else if (1 == l) {
                    dp[i][j] = s.charAt(i) == s.charAt(j);
                } else {
                    dp[i][j] = (s.charAt(i) == s.charAt(j) && dp[i + 1][j - 1]);
                }
                if (dp[i][j] && l + 1 > result.length()) {
                    result = s.substring(i, i + l + 1);
                }

            }
        }
        return result;
    }

    public static void main(String[] args) {
        LongestPalindrome_5 solution = new LongestPalindrome_5();
        String s = solution.longestPalindrome("babad");
        System.out.println(s);

    }
}

// @lc code=end
