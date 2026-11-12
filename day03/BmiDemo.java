import java.util.Scanner;

public class BmiDemo {
    public static void main(String[] args) {
        // 第 1 步：读入身高（米）和体重（公斤）——两个 double
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入身高:");
        double height = sc.nextDouble();
        System.out.println("请输入体重:");
        double weight = sc.nextDouble();
        // 提示：Scanner sc = new Scanner(System.in);  double h = sc.nextDouble();

        // 第 2 步：算 BMI = 体重 / (身高 * 身高)
        double bmi = weight / (height * height);

        // 第 3 步：判断等级
        //   BMI < 18.5          -> 偏瘦
        if (bmi < 18.5) {
            System.out.println("偏瘦");
        }
        //   18.5 <= BMI < 24    -> 正常
        else if (bmi >= 18.5 && bmi < 24) {
            System.out.println("正常");
        }
        //   24   <= BMI < 28    -> 超重
        else if (bmi >= 24 && bmi < 28) {
            System.out.println("超重");
        }
        //   BMI >= 28           -> 肥胖
        else {
            System.out.println("肥胖");
        }

        // 第 4 步：输出，保留两位两位小数
        System.out.println("BMI = " + String.format("%.2f", bmi));
        //   例：BMI = 22.86 → 正常

        //   提示：String.format("%.2f", bmi)
    }
}