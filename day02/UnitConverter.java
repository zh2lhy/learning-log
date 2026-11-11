
import java.util.Scanner;

public class UnitConverter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    while(true)
    {
        // 打印菜单（四行）
        System.out.println("1. 英寸->厘米");
        System.out.println("2. 摄氏->华氏");
        System.out.println("3. 公斤->磅");
        System.out.println("0. 退出");
        System.out.print("请选择：");
        int choice = sc.nextInt();

        if (choice == 0) {
            System.out.println("再见");
            break;
            // 跳出 while
        }

         switch (choice) {
            case 1:
                // 读英寸，算，打印
                System.out.print("输入英寸数：");
                double inch = sc.nextDouble();
                double cm = inch * 2.54;
                System.out.println(inch + " 英寸 = " + cm + " 厘米");
                break;             // 每个 case 后面必须有 break
            case 2:
                // 读摄氏，算，打印
                System.out.print("输入摄氏数：");
                double celsius = sc.nextDouble();
                double fahrenheit = celsius * (9.0 / 5) + 32;
                System.out.println(celsius + " 摄氏 = " + fahrenheit + " 华氏");
                break;
            case 3:
                // 读公斤，算，打印
                System.out.print("输入公斤数：");
                double kg = sc.nextDouble();
                double pound = kg * 2.2;
                System.out.println(kg + " 公斤 = " + pound + " 磅");
                break;
            default:
                System.out.println("没有这个选项");
        }
    }
    }
}

