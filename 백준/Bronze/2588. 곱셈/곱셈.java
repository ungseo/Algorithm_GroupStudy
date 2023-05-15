import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        int a, b;
        Scanner input = new Scanner(System.in);
        a = input.nextInt();
        b = input.nextInt();

        System.out.println(a * (b % 10));
        System.out.println(a * ((b / 10) % 10));
        System.out.println(a * (b / 100));
        System.out.println(a * b);
    }
}