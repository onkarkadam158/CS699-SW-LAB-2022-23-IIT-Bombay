#include<iostream>
using namespace std;
int subtract(int x,int y)
{
    int num1=x,num2=y;
<<<<<<< HEAD
    int s=num1*num2;
=======
    int s=num1 - num2;
>>>>>>> merge_example
    return s;
}
int main()
{
    int a,b;
    cin>>a>>b;
    int compute=subtract(a,b);
    cout<<compute;
    return 0;
}