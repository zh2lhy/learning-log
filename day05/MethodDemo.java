public class MethodDemo {

    // 有参数、有返回值
    static int add(int a, int b) {
        return a + b;
    }

    // 有参数、没有返回值
    static void sayHello(String name) {
        System.out.println("你好，" + name);
    }

    // 没有参数、有返回值
    static int answer() {
        return 42;
    }

    public static void main(String[] args) {
        sayHello("小明");                 // 1
        int x = add(3, 5);                // 2
        System.out.println(x);            // 3
        System.out.println(add(10, 20));  // 4
        System.out.println(answer());     // 5
        System.out.println(add(add(1, 2), add(3, 4)));  // 6
    }
}