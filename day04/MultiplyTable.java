/*
新建 day04\MultiplyTable.java，输出：

代码块


1*1=1
        1*2=2 2*2=4
        1*3=3 2*3=6 3*3=9
        ...
要求：共 9 行，第 i 行有 i 个式子，格式 j*i=结果，同一行内用空格隔开。

只给一句提示：两层 for 循环，外层是行 i，内层是列 j，j 从 1 到 i。 注意 print 不会换行，一行打印完要单独调用一次 println()。*/
public class MultiplyTable {
    public static void main(String[] args) {
        for (int i = 1; i <= 9; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(j+"*"+i+"="+i*j+" ");
            }
            System.out.println();
        }
    }
}
