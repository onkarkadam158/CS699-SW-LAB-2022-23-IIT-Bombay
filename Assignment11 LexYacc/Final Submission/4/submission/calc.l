%{
#include <stdlib.h>
#include <stdio.h>
void yyerror(char *);
#include "calc.tab.h"
%}

%%
([-]?[0-9])+ {
 yylval = atoi(yytext);
 return INTEGER;
 }
 
[-+()] return *yytext;
[ \t] ; /* skip whitespace */
. yyerror("invalid character");

%%

int yywrap(void) {
 return 1;
} 