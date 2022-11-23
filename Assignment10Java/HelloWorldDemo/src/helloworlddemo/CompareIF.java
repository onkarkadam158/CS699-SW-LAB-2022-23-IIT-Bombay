/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package helloworlddemo;

/**
 *
 * @author br
 */
public interface CompareIF<T> {

  /** Return -1 if this object is smaller than given object, +1 if
      vice versa, 0 if both are equal */
  int compare(T obj);

} // End interface CompareIF<T>
