package java_sub;

public class MyPow {
    public double myPow(double x, int n) {
        return n >= 0 ? quickMul(x, n) : 1.0 / quickMul(x, -n);
    }

    private double quickMul(double x, int n) {
        if (0 == n)
            return 1;
        double y = quickMul(x, n / 2);
        return n % 2 == 0 ? y * y : y * y * x;
    }
}
