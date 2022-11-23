/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package helloworlddemo;

/**
 *
 * @author br
 */
public class MyString implements CompareIF<MyString> {
    
    String s;
    
  public int compare(MyString a) {
    if(s.length() < a.s.length()) return -1;
    else if(s.length() > a.s.length()) return +1;
    else return 0;
  } // End compare()

    
}
