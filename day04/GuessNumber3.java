import java.util.Scanner;

public class GuessNumber3 {
    /*答案随机 1–100
    输入一个整数猜，提示 大了 或 小了
    最多只能猜 7 次
    猜中：输出 猜对了，第 N 次
7 次都没中：输出 没猜中，答案是 X，然后结束
    提示（只给思路，不给代码）：

    用 for (int i = 1; i <= 7; i++) 控制次数最省事；用 while 加计数变量也行
    每次循环里判断完三种情况后，猜中要立刻跳出
7 次循环自然结束、没有猜中，就会执行到循环后面的代码，那句话写在那里*/
//    答案随机 1–100
    public static void main(String[] args) {
        java.util.Random rand = new java.util.Random();
        int answer = rand.nextInt(100) + 1;   // 1~100
        //    输入一个整数猜，提示 大了 或 小了,最多只能猜 7 次
        int count = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入一个整数猜，提示 大了 或 小了,最多只能猜 7 次:");
        for (int i = 1; i <= 7; i++) {
            int guess = sc.nextInt();
            if (guess > answer) {
                System.out.println("猜的数字大了");
                count++;
            } else if (guess < answer) {
                System.out.println("猜的数字小了");
                count++;
            } else {
                System.out.println("猜对了，第 " + i + " 次");
                break;
            }

              if (count == 7) {
                System.out.println("没猜中，答案是 " + answer);
                break;
            }
        }
        }
    }


