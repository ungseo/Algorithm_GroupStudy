import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int Time, H, M, C;
        H = input.nextInt();
        M = input.nextInt();
        C = input.nextInt();
        Time = H * 60 + M + C;
        if (Time >= 24 * 60) {
            H = Time / 60 - 24;
            M = Time % 60;

        }
        else {
            H = Time / 60;
            M = Time % 60;
        }
        System.out.printf("%d %d", H, M);
    }
}