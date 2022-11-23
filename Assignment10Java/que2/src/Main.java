import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.Comparable;
public class Main {
    public static void main(String[] args) {
        String finalAnswer="ShortBuffer,SOAPBinding.Style,UUID";
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
//    Identify classes which implement the java.lang.Comparable interface and name any 3 of them.
//        You are given a file named "Solution.java" Write java code to create a file named it as "output.txt" and write your answer to it
//        write your answer in below format :
//        Class1,Class2,Class3