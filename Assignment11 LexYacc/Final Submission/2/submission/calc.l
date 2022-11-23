%{
#include <stdlib.h>
#include <stdio.h>
void yyerror(char *);
#include "calc.tab.h"

%}

%%
((-)*[0-9])+ {
 yylval = atoi(yytext);
 return INTEGER;
 }
 
[-+\n] return *yytext;
[ \t] ;
. ;
%%

int yywrap(void) {
 return 1;
} 