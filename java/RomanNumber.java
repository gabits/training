import  java.util.Scanner;
    
    
public class RomanNumber
{
    public static void main(String[]  args)
    {
        System.out.println(
            "Please enter an integer to convert into a Roman number:"
        );
        Scanner scan = new Scanner(System.in);
        int number = scan.nextInt();
        if ((number >= 1) && (number <= 3999))
        {
            String romanStr  = convert(number);
            System.out.println(
                "The converted number as Roman Numerals is "+ romanStr
            );
        }
        else
        {
            System.out.println("Number inputted was not in the range accepted");
        }
    }

    public static String convert(int  n)
    {
        String romanNumber = ""; 
        int thousands = (n / 1000);
        int hundreds = (n % 1000) / 100;
        int tens = (n % 100) /10;
        int units = (n %10);

        // First convert the thousands
        if (thousands >= 1)
        {
            // There is no need to give it numbers for the fifth
            // and tenth digit if the thousands digit is always
            // less or equal to 3
            romanNumber += romanDigit(thousands, "M", "", "");
        }
        // Then, convert the hundreds
        if (hundreds >= 1)
        {
            romanNumber += romanDigit(hundreds, "C", "D", "M");
        } 
        // Then the tens
        if (tens >= 1)
        {
            romanNumber += romanDigit(tens, "X", "L", "C");
        }
        // And at last the units
        if (units >= 1)
        {
            romanNumber += romanDigit(units, "I", "V", "X");
        }
        return romanNumber;
    }

    public static String romanDigit(int n, String one, String five, String ten)
    {
        String romanNumber = "";
        if (n <= 3)
        {
            int count = 1;
            while (count <= n)
            {
              romanNumber += one;
              count += 1;
            }
        }
        else if (n <= 4)
        {  
            romanNumber += one + five;
        }
        else if (n <= 5)
        {  
            romanNumber += five; 
        }
        else if (n <= 8)
        {  
            romanNumber += five;
            int count = 1;
            while (count <= (n - 5))
            {
              romanNumber += one;
              count += 1;
            }
        }
        else
        {  romanNumber += one + ten; }
        return romanNumber;
    }
}
