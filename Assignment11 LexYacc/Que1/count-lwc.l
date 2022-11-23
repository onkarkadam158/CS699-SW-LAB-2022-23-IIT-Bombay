%{
#include<stdio.h>
int linecount=0, wordcount=0 , charcount=0; 
%}
 
%%
\n linecount++; 
[^ \t\n]+ {wordcount++; charcount+=yyleng;}

%%

int main(){
yylex();
printf("%d %d %d",linecount,wordcount,charcount);
}
