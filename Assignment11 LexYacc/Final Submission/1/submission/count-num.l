%{
#include<stdio.h>
int numcount=0,floatcount=0; 
%}
 
%% 
[0-9]+ {numcount++;}
[0-9.0-9]+ {floatcount++;}
.
%%

int main(){
yylex();
printf("%d %d",numcount,floatcount);
}