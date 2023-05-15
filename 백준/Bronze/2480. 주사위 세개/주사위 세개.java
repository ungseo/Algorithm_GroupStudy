import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a,b,c, price;
        a = input.nextInt();
        b = input.nextInt();
        c = input.nextInt();
        if (a == b && b == c) {
            price = 10000 + a * 1000;


        } else if (a == b) {
            price = 1000 + a * 100;
        } else if (b == c) {
            price = 1000 + b * 100;

        } else if (a == c) {
            price = 1000 + a * 100;
        }
        else {
            price = Math.max(Math.max(a,b),c) * 100;
        }
        System.out.println(price);
    }



}