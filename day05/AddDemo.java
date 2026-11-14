public class AddDemo {

    // 重载 1：两个 int
    static int add(int a, int b) {

        // ??? 你写
        return a + b;

    }

    // 重载 2：两个 double
    static double add(double a, double b) {

        // ??? 你写
        return a + b;

    }

    // 重载 3：三个 int
    static int add(int a, int b, int c) {

        // ??? 你写
        return a + b + c;

    }

    public static void main(String[] args) {
        System.out.println(add(1, 2));          // 期望 3
        System.out.println(add(1.5, 2.5));      // 期望 4.0
        System.out.println(add(1, 2, 3));       // 期望 6
    }
}