import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        FileReader fileReader=new FileReader("log.txt");
        BufferedReader bufferedReader=new BufferedReader(fileReader);
        SortedSet<String> dataSet = new TreeSet<String> ();

        while (bufferedReader.ready()){
            String temp = bufferedReader.readLine();
            dataSet.add(temp);
            //System.out.println(temp);
        }
//        System.out.println("sorted set started\n\n\n\n");
        Iterator<String> iteratorOfdataSet = dataSet.iterator();
        while (iteratorOfdataSet.hasNext())
            System.out.println(iteratorOfdataSet.next());
        bufferedReader.close();
        fileReader.close();
    }
}

//Statement
//
//        Instructions for question 3 onwards
//
//                In a network, there are several machines (called nodes). Each of these have an id. Each of them is creating a log of events. For the purpose of this lab, we are going to assume as input to our Java program, a log file which is the result of the merger of all the log entries from each of the network machines. The log file name is given as command-line argument to the Java program.
//                The format of the input log file is that it has a series of lines. Each line has 5 entries, separated by a space: (1) Network node-id, (2) The node's log entry number, (3) Log-entry type, (4) Log-entry value, (5) Timestamp of the log-entry. All the five fields are long integers (64 bit).
//                An example log file is given. As you can see, the log entries can occur in the log file in any order. And there can be duplicates as well.
//
//
//                Some rules:
//                1.You MUST NOT write code to do file reading or line parsing apart from using routines of BufferedReader and StringTokenizer.
//                2.Also, you MUST NOT write any explicit code to do duplicate detection, or sorting: you must make the collections framework data structures do such work for you.
//                3.AVOID using elaborate data structures outside of the Java collections framework (e.g. do not use arrays or Vectors or such similar data structures from other Java libraries).
//
//                Hints:
//                1.Proceed in steps, if you are new to Java.
//                2.Start with some simple Hello World.
//                3.Go through the examples given in the video tutorial.
//                Online examples/tutorials may help (but may also confuse more).
//                4.Learn to use String, StringTokenizer, BufferedReader, FileReader, etc. one by one, in separate simple examples.
//                You may have to use "import" statements to use java libraries; such as "import java.io.*", "import java.util.*". These are similar to #include statements in C/C++.
//                5.Go through the collections framework tutorial mentioned in the references.
//                6.Learn from simple examples given in the above tutorial.
//                7.Our solution for the above problem was less than a total of 100 lines of code, including comments.


//    In Parse1.java, read each line of the log file.
//        You would have to use BufferedReader, String (from the java library) as part of this process.
//        Insert the entries which you have read into an appropriate data structure, from the existing collections framework.
//        While inserting, ensure that duplicates are not stored and also each line of log file is sorted (according to String comparison).
//        (hint: use something which implements the Set interface or its extension).
//        print after following above steps on stdout in same format as given in log.txt