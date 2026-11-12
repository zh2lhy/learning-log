import java.util.Scanner;

public class GradeDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入分数（0-100）:");
        int score = sc.nextInt();

        // 要求：
        //   先判断是否合法（score < 0 || score > 100），再按档位往下判
        if (score < 0 || score > 100) {
            System.out.println( "分数 " + score + " -> 分数不合法");
            return;
        }
        //   90-100 -> A 优秀
        if (score >= 90) {
            System.out.println( "分数 " + score + " -> A 优秀");
        }
        //   80-89  -> B 良好
        else if (score >= 80 ) {
            System.out.println( "分数 " + score + " -> B 良好");
        }
        //   70-79  -> C 中等
        else if (score >= 70 ) {
            System.out.println( "分数 " + score + " -> C 中等");
        }
        else if (score >= 60 ) {
            System.out.println( "分数 " + score + " -> D 及格");
        }
        else if (score >= 0 ) {
            System.out.println( "分数 " + score + " -> E 不及格");
        }

               //
        // 输出格式：
        //   分数 85 -> B 良好
        //   分数 120 -> 分数不合法
        //
        // 提示：先判断是否合法（score < 0 || score > 100），再按档位往下判

    }
}