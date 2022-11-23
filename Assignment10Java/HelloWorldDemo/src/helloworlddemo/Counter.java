/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package helloworlddemo;

/**
 *
 * @author br
 */
class Counter implements Incrementable, CompareIF<Counter> {

  int count;

  Counter() {
    count = 0;
  } // End constructor Counter()

  void add(int x) {
    count += x;
  } // End add()

  public void increment() {
    count++;
  } // End increment()

  public int compare(Counter c1) {
    if(count < c1.count) return -1;
    else if(count > c1.count) return +1;
    else return 0;
  } // End compare()

  public static void main2(String argv[]) {

    if(argv.length != 1) {
      System.err.println("Need one argument");
      System.exit(1);
    }

    Counter c1 = new Counter();
    c1.add(10);
    c1.increment();

    System.out.println("Counter value is " + c1.count);

    Counter c2 = new Counter();
    c2.add(Integer.parseInt(argv[0]));

    System.out.println("compare = " + c1.compare(c2));

  } // End main()

} // End class Counter
