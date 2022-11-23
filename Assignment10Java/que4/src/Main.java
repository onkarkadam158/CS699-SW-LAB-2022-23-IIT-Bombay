import java.util.*;
import java.io.*;
class log implements Comparable<log>{
    long field1;
    long field2;
    long field3;
    long field4;
    long field5;
    // constructor
    log(long field1, long field2, long field3, long field4, long field5) {
        this.field1 = field1;
        this.field2 = field2;
        this.field3 = field3;
        this.field4 = field4;
        this.field5 = field5;
    }
    @Override
    public int compareTo(log input) {
        if (this.field1 != input.field1) {
            if(this.field1==input.field1)
                return 0;
            else if(this.field1 > input.field1)
                return 1;
            else
                return -1;
        }
        else {
            if(this.field2==input.field2)
                return 0;
            else if(this.field2 > input.field2)
                return 1;
            else
                return -1;
        }
    }
}

public class Main {

    public static void main(String[] args) throws IOException {
//        String fileName = args[0];
        FileReader fileReader=new FileReader("log.txt");
        BufferedReader bufferedReader=new BufferedReader(fileReader);
        SortedSet<String> dataSet = new TreeSet<String> ();

        while (bufferedReader.ready()){
            String temp = bufferedReader.readLine();
            dataSet.add(temp);
//            System.out.println(temp);
        }
//        data reading and duplicate removal done above

        SortedSet<log> newdataSet = new TreeSet<log> ();
        Iterator<String> iteratorOfdataSet = dataSet.iterator();

        while (iteratorOfdataSet.hasNext()) {
            String nextIndataset = iteratorOfdataSet.next();
            StringTokenizer st = new StringTokenizer(nextIndataset," ");
            //tokenizing a single entry into 5 column parts
            long field1,field2,field3,field4,field5;
            field1 = Long.parseLong(st.nextToken());
            field2 = Long.parseLong(st.nextToken());
            field3 = Long.parseLong(st.nextToken());
            field4 = Long.parseLong(st.nextToken());
            field5 = Long.parseLong(st.nextToken());
            log tempObj = new log(field1, field2, field3, field4, field5);
            newdataSet.add(tempObj);
//            System.out.println(tempObj.field2);
        }
        //printing out the final output
        for(log d:newdataSet){
            System.out.println(d.field1+" "+d.field2+" "+d.field3+" "+d.field4+" "+d.field5);
        }
        bufferedReader.close();
        fileReader.close();
    }
}

//
//    Now in Parse2.java again read the log file and parse each line. You would have to use BufferedReader, String, and StringTokenizer (from the java library)
//    as part of this process.
//    Insert the entries which you have read into an appropriate data structure,
//    from the existing collections framework. While inserting, ensure that duplicates are not stored (hint: use something which implements the Set interface or its extension).
//        After finishing reading the file, print the log entries onto stdout, in the same 5-column format as the input file.
//        You must print the entries in increasing order of node ids. And within the same node id, you must print entries in order of increasing log entry number.
//        In doing this, you must use the for each loop, or an appropriate iterator.
//        To achieve the correct ordering of entries in the output, you must use an object called Log to represent each log entry,
//        and the object must implement the Comparable interface.
//
//
