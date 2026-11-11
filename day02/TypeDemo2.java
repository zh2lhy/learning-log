public class TypeDemo2 {
    public static void main(String[] args) {
        System.out.println(Integer.MAX_VALUE);
        System.out.println(Integer.MAX_VALUE + 1);   // 溢出：到顶绕回负数
        System.out.println(10 / 3);                  // 整数除法，砍掉小数
        System.out.println(10 % 3);                  // 取余
        System.out.println(10 / 3.0);                // 有一个是小数，结果才是小数
        char c = 'A';
        System.out.println(c + 1);                   // char 本质是数字，A=65
        System.out.println((char) (c + 1));          // 强制转回字符
        System.out.println(0.1 + 0.2);               // 浮点存不准
        System.out.println((int) 3.99);              // 强转是截断，不是四舍五入
    }
}   //()