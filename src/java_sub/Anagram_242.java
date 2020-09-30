package java_sub;

public class Anagram_242 {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] tables = new int[26];
        for (int i = 0; i < s.length(); i++) {
            tables[s.charAt(i) - 'a']++;
        }
        for (int i = 0; i < t.length(); i++) {
            int temp = --tables[t.charAt(i) - 'a'];
            if (temp < 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        TestCase case1 = new TestCase();
        case1.isAnagram("a", "b");

    }
}
