import java.util.Scanner;

public class GuessNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 测试阶段先把答案写死成 42，逻辑全对了再改成随机数
        java.util.Random rand = new java.util.Random();
        int answer = rand.nextInt(100) + 1;   // 1~100
        int count = 0;

        System.out.println("猜一个 1-100 的数");

        // while (true) 就是一直转，直到遇到 break
        while (true) {
            System.out.print("你猜：");
            int guess = sc.nextInt();
            count++;

            // TODO 1：猜大了
            if (guess > answer) {
                System.out.println("你猜的数大了");   // 提示"大了"
            }
            // TODO 2：猜小了
            else if (guess < answer) {
                System.out.println("你猜的数小了");   // 提示"小了"
            }
            // 猜中
            else {
                System.out.println("猜对了，一共猜了 " + count + " 次");
                break;                     // 跳出循环，程序结束
            }
        }
    }
}