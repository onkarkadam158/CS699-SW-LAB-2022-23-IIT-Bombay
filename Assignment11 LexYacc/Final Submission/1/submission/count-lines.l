%{
#include<stdio.h>
int linecount=0;
%}
 
%%
\n {linecount++;} 
. 
%%

int main(){
yylex();
printf("%d",linecount);
}