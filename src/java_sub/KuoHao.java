package java_sub;

import java.util.ArrayList;
import java.util.List;

public class KuoHao {
    public ArrayList<String> result = new ArrayList<>();

    public List<String> generateParenthesis(int n) {
        _generate(0, 0, n, "");
        return result;
    }

    private void _generate(int left, int right, int max, String current_str) {
        // teminator
        if (left == max && right == max) {
            result.add(current_str);
            return;
        }
        // process
        String current_str1 = current_str + "(";
        String current_str2 = current_str + ")";
        // drivil down
        if (left < max)
            _generate(left + 1, right, max, current_str1);
        if (right < left)
            _generate(left, right + 1, max, current_str2);
        // clear
    }

    public static void main(String[] args) {
        KuoHao kuoHao = new KuoHao();
        List<String> result = kuoHao.generateParenthesis(3);

        System.out.println(result);

    }
}
