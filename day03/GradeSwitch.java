import java.util.Scanner;

public class GradeSwitch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入分数（0-100）:");
        int score = sc.nextInt();

        if (score < 0 || score > 100) {
            System.out.println("分数 " + score + " -> 分数不合法");
            return;
        }

        // 用 switch 重写成绩等级：
        //   先算十位：
             int level = score / 10;
        switch (level) {

        //   level 是 10 或 9 -> A 优秀
        case 10:
        case 9:
            System.out.println("分数 " + score + " -> A 优秀");
            break;
        //   level 是 8       -> B 良好
        case 8:
            System.out.println("分数 " + score + " -> B 良好");
            break;
        case 7:
            System.out.println("分数 " + score + " -> C 中等");
            break;
        case 6:
            System.out.println("分数 " + score + " -> D 及格");
            break;
        default:
            System.out.println("分数 " + score + " -> E 不及格");
            break;
        }
        //   level 是 6       -> D 及格
        //   其它（0-5）      -> E 不及格
        //
        // 输出格式和上一版一样：分数 85 -> B 良好
        //
        // 提示：两个 case 要共用一段代码，就上下并排写：
        //   case 10:
        //   case 9:
        //       System.out.println("A");
        //       break;

    }
}