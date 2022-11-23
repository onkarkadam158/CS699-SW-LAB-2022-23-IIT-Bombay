/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package helloworlddemo;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/**
 *
 * @author br
 */
public class HelloWorld {

  public static void sort(CompareIF[] A) {
      for(int i = 0; i < A.length-1; i++) {
          for(int j = i+1; j < A.length; j++) {
              if(A[i].compare(A[j]) == 1) {
                  CompareIF temp = A[i];
                  A[i] = A[j];
                  A[j] = temp;
              }
          }
      }
  } // End sort()

  public static void main(String argv[]) {

    System.out.println("Hello World");

    System.out.println("Number of arguments is " + argv.length);

    for(int i = 0; i < argv.length; i++) {
      System.out.println("Argument " + i + " is " + argv[i]);
      java.io.File f1 = new java.io.File(argv[i]);
      System.out.println("File " + argv[i] + " exists = " + f1.exists());
    }


    for(int i = 0; i < 10; i++) {
      System.out.println(Math.random());
    }

    try {
      BufferedReader fin = new BufferedReader(new FileReader("../testfile1"));
      String s2 = fin.readLine();
      System.out.println(s2);
    } catch(IOException ioe) {
      ioe.printStackTrace();
      System.err.println(ioe.getMessage());
    }

    Counter[] myCounters = new Counter[5];
    myCounters[0] = new Counter(); myCounters[0].add(1);
    myCounters[1] = new Counter(); myCounters[1].add(-2);
    myCounters[2] = new Counter(); myCounters[2].add(14);
    myCounters[3] = new Counter(); myCounters[3].add(3);
    myCounters[4] = new Counter(); myCounters[4].add(6);

    MyString[] myS = new MyString[5];
    myS[0] = new MyString(); myS[0].s = new String("abcd");
    myS[1] = new MyString(); myS[1].s = new String("a");
    myS[2] = new MyString(); myS[2].s = new String("ab");
    myS[3] = new MyString(); myS[3].s = new String("efghij");
    myS[4] = new MyString(); myS[4].s = new String("xyz");

    sort(myCounters);
    for(int i = 0; i < myCounters.length; i++) {
        System.out.print(myCounters[i].count + ",");
    }
    System.out.println();

    sort(myS);
    for(int i = 0; i < myS.length; i++) {
        System.out.print(myS[i].s + ",");
    }
    System.out.println();

  } // End main()

} // End class HelloWorld
