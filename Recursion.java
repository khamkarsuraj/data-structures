/* Recursion */
// This code is to understand recursion concept.

// Steps:   1. Base condition
//          2. function call as per logic

public class Recursion {
    // This function will sum values from 1 to N.
    public int sumFrom1ToN(int n) {
        //Always this about base condition first
        if (n == 1) {
            return 1;
        }
        //Think about logic you want
        return this.sumFrom1ToN(n - 1) + n;
    }

    public int fibonacciSeries(int n) {
        //Base condition: 1st and 2nd element would be 1
        if (n <= 2) {
            return 1;
        }
        //otherwise sum of previous two numbers
        return fibonacciSeries(n-1) + fibonacciSeries(n-2);
    }

    public int frogProblem(int n, int sum) {
        //Base condition: 1st and 2nd element would be 1
        if (n <= 2) {
            return 1;
        }
        //otherwise sum of previous two numbers
        return fibonacciSeries(n-1) + fibonacciSeries(n-2);
    }

    public void printNtoOne(int n) {
        if (n == 1) {
            System.out.print(1 + " ");
            return;
        }
        System.out.print(n + " ");
        printNtoOne(n-1);
    }

    public void printOnetoN(int n) {
        if (n == 1) {
            System.out.print(1 + " ");
            return;
        } 
        printOnetoN(n-1);
        System.out.print(n + " ");
    }

    public static void main(String[] args) {
        Recursion s = new Recursion();
        System.out.println("Sum: " + s.sumFrom1ToN(10) + "\n");
        
        System.out.println("Fibonacci: " + s.fibonacciSeries(5) + "\n");
        
        System.out.println("Frog: " + s.frogProblem(11+1, 0) + "\n");
        
        System.out.println("Print N to 1");
        s.printNtoOne(5);
        System.out.println("\n");

        System.out.println("Print 1 to N");
        s.printOnetoN(5);
        System.out.println();
    }
}
