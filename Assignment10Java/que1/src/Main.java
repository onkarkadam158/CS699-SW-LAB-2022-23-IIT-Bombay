import java.io.BufferedWriter;
import java.io.FileWriter;
import java.lang.String;

import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        String finalAnswer="Comparable<String>\nSerializable\nCharSequence\n";
        try {
            BufferedWriter out = new BufferedWriter(
                    new FileWriter("output.txt"));
            out.write(finalAnswer);
            out.close();
        } catch (IOException e) {
            System.out.println("Exception Occurred" + e);
        }
    }
}

//Statement
//
//    Identify the interfaces implemented by java.lang.String.
//        Write a java code in file "Solution.java" to create a new file named as "output.txt" and write your answer to it.
//        write each interface in new line
//        Example :
//        Interface1
//        Interface2
//
//        so on
//        Give a newline after your last interface