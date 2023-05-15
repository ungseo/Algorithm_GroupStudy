import java.util.Scanner;
 class Main {
     public static void main(String[] args) {
         int A, B;
         Scanner input = new Scanner(System.in);
         A = input.nextInt();
         B = input.nextInt();
         
         if (A > B) {
             System.out.println('>');
         } else if (A == B) {
             System.out.println("==");
             
         } else {
             System.out.println('<');
         }
     }
 }