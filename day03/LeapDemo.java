import java.util.Scanner;

public class LeapDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入年份:");
        int year = sc.nextInt();

        // 闰年规则（满足任意一条就是闰年）：
        //   ① 能被 4 整除，且不能被 100 整除
        if (year % 4 == 0 && year % 100 != 0) {
            System.out.println(year + " 是闰年");
        }

        //   ② 能被 400 整除
        else if (year % 400 == 0) {
            System.out.println(year + " 是闰年");
        }
        else {
            System.out.println(year + " 不是闰年");
        }
        //
        // 输出格式：
        //   2024 是闰年
        //   1900 不是闰年
        //
        // 提示：% 取余（判断能不能整除）；&& 并且；|| 或者

    }
}