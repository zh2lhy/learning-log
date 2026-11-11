//0:00–0:35 八种基本类型、类型转换（自动/强制）、运算符、字符串拼接
public class TypeDemo1 {
    public static void main(String []args){

        //        整数型
        short a = 127;
        int b = 520;
        long c = 1314;//小转大自动完成，由int转向long;
        long d = 100000000000L;//这个数超出in范围了；long后面的数必须加L.

        //        小数型
        float e = 1.2f;//单精度浮点数 4字节 6位有效数字;float后面必须加F
        double f = 1.2;//双精度浮点数 8字节 15位有效数字

        //        字符型
        char g = 'A';


        //        布尔型
        boolean h = true;



        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(d);
        System.out.println(e);
        System.out.println(f);
        System.out.println(g);
        System.out.println(h);
    }
}
