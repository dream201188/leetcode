package java_sub;

public class Roma_12 {
    public String intToRoman(int num) {
        int[] nums = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
        String[] romaStr = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };

        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < nums.length; i++) {
            if (num < 0)
                break;
            int count = num / nums[i];
            for (int j = 0; j < count; j++) {
                num -= nums[i];
                sb.append(romaStr[i]);
            }
        }
        return sb.toString();

    }

    public static void main(String[] args) {
        Roma_12 roma_12 = new Roma_12();
        String result = roma_12.intToRoman(1994);
        System.out.println(result);
    }
}