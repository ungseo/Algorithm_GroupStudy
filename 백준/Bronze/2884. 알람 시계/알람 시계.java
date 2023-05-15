import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int H, M;
        H = input.nextInt();
        M = input.nextInt();
        int Time;
        Time = H * 60 + M - 45;
        if (Time >= 0) {
            H = Time / 60;
            M = Time % 60;
        } else {
            H = 23;
            M = Time % 60 + 60;
        }

        System.out.printf("%d %d", H,M);

    }
}