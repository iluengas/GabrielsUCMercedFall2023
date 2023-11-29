// STEP: Import required packages
import java.sql.*;
import java.io.FileWriter;
import java.io.PrintWriter;

public class Lab_9 {
    private Connection c = null;
    private String dbName;
    private boolean isConnected = false;

    private void openConnection(String _dbName) {
        dbName = _dbName;

        if (false == isConnected) {
            System.out.println("++++++++++++++++++++++++++++++++++");
            System.out.println("Open database: " + _dbName);

            try {
                String connStr = new String("jdbc:sqlite:");
                connStr = connStr + _dbName;

                // STEP: Register JDBC driver
                Class.forName("org.sqlite.JDBC");

                // STEP: Open a connection
                c = DriverManager.getConnection(connStr);

                // STEP: Diable auto transactions
                c.setAutoCommit(false);

                isConnected = true;
                System.out.println("success");
            } catch (Exception e) {
                System.err.println(e.getClass().getName() + ": " + e.getMessage());
                System.exit(0);
            }

            System.out.println("++++++++++++++++++++++++++++++++++");
        }
    }

    private void closeConnection() {
        if (true == isConnected) {
            System.out.println("++++++++++++++++++++++++++++++++++");
            System.out.println("Close database: " + dbName);

            try {
                // STEP: Close connection
                c.close();

                isConnected = false;
                dbName = "";
                System.out.println("success");
            } catch (Exception e) {
                System.err.println(e.getClass().getName() + ": " + e.getMessage());
                System.exit(0);
            }

            System.out.println("++++++++++++++++++++++++++++++++++");
        }
    }

    private void create_View1() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Create V1");

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void Q1() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Q1");

        try {
            FileWriter writer = new FileWriter("output/1.out", false);
            PrintWriter printer = new PrintWriter(writer);
                
            printer.printf("%s|%s\n", "country", "cnt");

            printer.close();
            writer.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void create_View2() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Create V2");

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void Q2() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Q2");

        try {
            FileWriter writer = new FileWriter("output/2.out", false);
            PrintWriter printer = new PrintWriter(writer);

            printer.printf("%s|%s\n", "customer", "cnt");

            printer.close();
            writer.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void Q3() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Q3");

        try {
            FileWriter writer = new FileWriter("output/3.out", false);
            PrintWriter printer = new PrintWriter(writer);

            printer.printf("%s|%s\n", "customer", "total_price");

            printer.close();
            writer.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void create_View4() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Create V4");

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void Q4() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Q4");

        try {
            FileWriter writer = new FileWriter("output/4.out", false);
            PrintWriter printer = new PrintWriter(writer);

            printer.printf("%s|%s\n", "supplier", "cnt");

            printer.close();
            writer.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void Q5() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Q5");

        try {
            FileWriter writer = new FileWriter("output/5.out", false);
            PrintWriter printer = new PrintWriter(writer);

            printer.printf("%s|%s\n", "country", "cnt");

            printer.close();
            writer.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void Q6() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Q6");

        try {
            FileWriter writer = new FileWriter("output/6.out", false);
            PrintWriter printer = new PrintWriter(writer);

            printer.printf("%s|%s|%s\n", "supplier", "priority", "parts");

            printer.close();
            writer.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void Q7() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Q7");

        try {
            FileWriter writer = new FileWriter("output/7.out", false);
            PrintWriter printer = new PrintWriter(writer);

            printer.printf("%s|%s|%s\n", "country", "status", "orders");

            printer.close();
            writer.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void Q8() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Q8");

        try {
            FileWriter writer = new FileWriter("output/8.out", false);
            PrintWriter printer = new PrintWriter(writer);

            printer.printf("%s\n", "clerks");

            printer.close();
            writer.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void Q9() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Q9");

        try {
            FileWriter writer = new FileWriter("output/9.out", false);
            PrintWriter printer = new PrintWriter(writer);

            printer.printf("%s|%s\n", "country", "cnt");

            printer.close();
            writer.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void create_View10() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Create V10");

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void Q10() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Q10");

        try {
            FileWriter writer = new FileWriter("output/10.out", false);
            PrintWriter printer = new PrintWriter(writer);

            printer.printf("%s|%s|%s\n", "part_type", "min_disc", "max_disc");

            printer.close();
            writer.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void create_View111() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Create V111");

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void create_View112() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Create V112");

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void Q11() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Q11");

        try {
            FileWriter writer = new FileWriter("output/11.out", false);
            PrintWriter printer = new PrintWriter(writer);

            printer.printf("%s\n", "order_cnt");

            printer.close();
            writer.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void Q12() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Q12");

        try {
            FileWriter writer = new FileWriter("output/12.out", false);
            PrintWriter printer = new PrintWriter(writer);

            printer.printf("%s|%s\n", "region", "max_bal");

            printer.close();
            writer.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void Q13() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Q13");

        try {
            FileWriter writer = new FileWriter("output/13.out", false);
            PrintWriter printer = new PrintWriter(writer);

            printer.printf("%s|%s|%s\n", "supp_region", "cust_region", "min_price");

            printer.close();
            writer.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void Q14() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Q14");

        try {
            FileWriter writer = new FileWriter("output/14.out", false);
            PrintWriter printer = new PrintWriter(writer);

            printer.printf("%s\n", "items");

            printer.close();
            writer.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void Q15() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Q15");

        try {
            FileWriter writer = new FileWriter("output/15.out", false);
            PrintWriter printer = new PrintWriter(writer);

            printer.printf("%s|%s|%s\n", "region", "supplier", "acct_bal");

            printer.close();
            writer.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    public static void main(String args[]) {
        Lab_9 sj = new Lab_9();
        
        sj.openConnection("tpch.sqlite");

        sj.create_View1();
        sj.Q1();

        sj.create_View2();
        sj.Q2();

        sj.Q3();

        sj.create_View4();
        sj.Q4();

        sj.Q5();
        sj.Q6();
        sj.Q7();
        sj.Q8();
        sj.Q9();

        sj.create_View10();
        sj.Q10();

        sj.create_View111();
        sj.create_View112();
        sj.Q11();

        sj.Q12();
        sj.Q13();
        sj.Q14();
        sj.Q15();

        sj.closeConnection();
    }
}
