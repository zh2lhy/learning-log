public class TypeDemo3 {
    public static void main(String[] args) {
        //类型转换(自动/强制)
        int a = 10;
        long b = a; //自动转换,由int转向long，大转小自动完成
        System.out.println(b);
        System.out.println(b);
        System.out.println(a);
        //强制转换(由大转向小)
        int c = (int)b;//强制转换,由long转向int;大转小需要强制转换
        System.out.println(c);
        System.out.println(b);
        System.out.println(a);
        //强制转换(由小转向大)
        long d = (long)a;//强制转换,由int转向long;小转大需要强制转换
        System.out.println(d);
        System.out.println(a);
        System.out.println(b);
    }
}
