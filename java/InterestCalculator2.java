import java.util.Scanner;


public class InterestCalculator2 {
    public static void main(String[] arg) 
    {
        double initialBalance = 10000;
        
        System.out.println("Please enter a savings target");
        Scanner scan = new Scanner(System.in);
        double savingsTarget = scan.nextDouble();
        System.out.println("The initial balance is: £" + initialBalance);
        double currentBalance = initialBalance + interestOn(initialBalance);
        
        System.out.println("The balance after 1 year is: £" + currentBalance );
        if(currentBalance > savingsTarget)
        {
             System.out.println("Congratulations, your savings target has been reached");
        }
        currentBalance = currentBalance + interestOn(currentBalance );
        System.out.println("The balance after 2 years is: £" + currentBalance);
        if(currentBalance > savingsTarget)
        {
             System.out.println("Congratulations, your savings target has been reached");
        }
        currentBalance = currentBalance + interestOn(currentBalance);
        System.out.println("The balance after 3 years is: £" + currentBalance);
        if(currentBalance > savingsTarget)
        {
             System.out.println("Congratulations, your savings target has been reached");
        }
    }

    public static double interestOn(double balance)
    {
        double interest = balance*.05;
        return interest;
    }
}