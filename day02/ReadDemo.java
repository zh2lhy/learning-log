import java.util.Scanner;

public class ReadDemo {
    public static void main(String[] args) {
        // 1. 创建 Scanner，接键盘输入
        Scanner a = new Scanner(System.in);
        // 2. 读一个 double 存进变量
        double b = a.nextDouble();
        // 3. 打印这个变量
        System.out.println(b);
    }
}
