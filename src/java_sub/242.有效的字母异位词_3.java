/*
 * @lc app=leetcode.cn id=242 lang=java
 *
 * [242] 有效的字母异位词
 * 使用字母的阿斯克码作为数组的index，出现次数作为value，如果两个是异位词那么数组的每个值应该是相等的
 */

// @lc code=start
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        char[] sTables = new char[26];
        char[] tTables = new char[26];
        for (int i = 0; i < s.length(); i++) {
            sTables[s.charAt(i) - 'a']++;
        }
        for (int i = 0; i < t.length(); i++) {
            tTables[t.charAt(i) - 'a']++;
        }
        for (int i = 0; i < 26; i++) {
            if (sTables[i] != tTables[i]) {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end
