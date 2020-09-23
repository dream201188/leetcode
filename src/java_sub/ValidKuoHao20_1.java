package java_sub;

import java.util.HashMap;
import java.util.Stack;

public class ValidKuoHao20_1 {

    public boolean isValid(String s) {

        if (s.length() % 2 == 1)
            return false;

        Stack<String> stack = new Stack<>();
        HashMap<String, String> pairs = new HashMap<String, String>() {
            /**
             *
             */
            private static final long serialVersionUID = 1L;

            {
                put("}", "{");
                put(")", "(");
                put("]", "[");
            }
        };
        for (int i = 0; i < s.length(); i++) {
            String ch = s.substring(i, i + 1);
            if (pairs.containsKey(ch)) {
                if (stack.isEmpty() || !stack.peek().equals(ch))
                    return false;
                else
                    stack.pop();
            } else
                stack.push(ch);

        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        ValidKuoHao20 soultion = new ValidKuoHao20();
        boolean flag = soultion.isValid("((])){[]}");
        System.out.println(flag);
    }
}