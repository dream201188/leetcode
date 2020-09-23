package java_sub;

public class ClimbStairs {

    public int climbStairs(int n) {
        if (n < 2) {
            return n;
        }
        int a = 1, b = 1, c = 2;
        for (int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }

    public static void main(String[] args) {
        ClimbStairs climbStairs = new ClimbStairs();
        int n = climbStairs.climbStairs(5);
        System.out.println(n);

    }
}
