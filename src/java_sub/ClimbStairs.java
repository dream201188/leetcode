package java_sub;

public class ClimbStairs {

    public int climbStairs(int n) {
        int a = 1, b = 1;
        while (n-- > 0)
            a = (b += a) - a;
        return a;
    }

    public static void main(String[] args) {
        ClimbStairs climbStairs = new ClimbStairs();
        int n = climbStairs.climbStairs(5);
        System.out.println(n);

    }
}
