/*
 * @lc app=leetcode.cn id=242 lang=java
 *
 * [242] 有效的字母异位词
 * 使用字母的阿斯克码作为数组的index，出现次数作为value，如果两个是异位词那么数组的每个值最后应该是0
 */

// @lc code=start
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        char[] tables = new char[26];
        for (int i = 0; i < s.length(); i++) {
            tables[s.charAt(i) - 'a']++;
            tables[t.charAt(i) - 'a']--;
        }
        for (int num : tables) {
            if (num != 0) {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end
