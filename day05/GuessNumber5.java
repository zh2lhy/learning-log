import java.util.Scanner;

public class GuessNumber5 {

    // 方法 1：比大小，返回提示语（你写的，保留原样）
    static String compare(int guess, int answer) {
        if (guess > answer) {
            return "猜的数字大了";
        }
        else if (guess < answer) {
            return "猜的数字小了";
        }
        else {
            return "猜对了";
        }
    }


    // 方法 2：玩一局（你来写）
    //       每轮读一个数，用 compare() 拿提示
    //       猜中 -> 打印 "猜对了，第 N 次"，然后结束这一局
    //       7 次都没中 -> 循环结束后打印 "没猜中，答案是 X"
    static void play() {
//        答案随机 1~100
        java.util.Random rand = new java.util.Random();
        int answer = rand.nextInt(100) + 1;   // 1~100
        int count = 0;
        Scanner sc = new Scanner(System.in);
        while (count <= 7) {
            System.out.print("你猜：");
            int guess = sc.nextInt();
            String result = compare(guess,answer);
            count++;
            if (result.equals("猜对了")) {
                System.out.println("猜对了，第 " + count + " 次");
                break;
            }
            if(count == 7) {
                System.out.println("没猜中，答案是 " + answer);
                break;
            }
            System.out.println(result);


               }

        // ???  这里你来写

    }

    public static void main(String[] args) {
        play();   // main 里只剩这一行
    }
}