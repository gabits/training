public class InterestCalculator
{
   public static void main(String[] args)
   {
      double initialBalance = 10000;
      double currentBalance = initialBalance;
      System.out.println("The initial balance is: £" + initialBalance);
      // year 1
      currentBalance = currentBalance + interestOn(currentBalance); 
      // curent balance = 10500
      System.out.println("The balance after 1 year is: £" + currentBalance);
      // year 2
      currentBalance = currentBalance + interestOn(currentBalance); 
      // current balance = 11025
      System.out.println("The balance after 2 year is: £" + currentBalance);
      // year 3
      currentBalance = currentBalance + interestOn(currentBalance); 
      System.out.println("The balance after 3 year is: £" + currentBalance);

   }        
   public static double interestOn(double balance)
   {
       double interest = balance * 0.05;
       return interest;
   }
}