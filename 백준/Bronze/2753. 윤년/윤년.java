import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        int A;
        Scanner input = new Scanner(System.in);
        A = input.nextInt();
        if ((A % 4 == 0 && A % 100 != 0) || A % 400 == 0) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}