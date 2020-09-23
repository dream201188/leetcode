package java_sub;

import java.util.Stack;
public class ValidKuoHao {

    public boolean checkValidString(String s) {
        Stack<Integer> left = new Stack<>();
        Stack<Integer> star = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            String target_char = s.substring(i, i + 1);
            if ("(".equals(target_char)) {
                left.push(i);
                continue;
            }
            if ("*".equals(target_char)) {
                star.push(i);
                continue;
            }
            if (")".equals(target_char)) {
                if (!left.isEmpty()) {
                    left.pop();
                    continue;
                }
                if (!star.isEmpty()) {
                    star.pop();
                    continue;
                }
                return false;

            }

        }
        while (!left.isEmpty()) {
            if (star.isEmpty())
                return false;

            if (left.peek() > star.peek())
                return false;

            else {
                left.pop();
                star.pop();
            }

        }
        return true;

    }

    public static void main(String[] args) {
        ValidKuoHao soultion = new ValidKuoHao();
        boolean flag = soultion.checkValidString(")(");
        System.out.println(flag);
    }
}