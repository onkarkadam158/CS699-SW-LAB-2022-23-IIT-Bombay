/* Definitions */

%{
#include <stdio.h>
%}

%token BOOLEAN
%token OR
%token AND
%token NOT

%left OR
%left AND

%%

prog:
prog stmt
|
;


stmt:
expr ';' { fprintf(stderr, "Expr value is %d\n", $1); }
;

expr:
BOOLEAN { $$ = $1; }
| expr AND expr { $$ = $1 && $3; }
| expr OR expr { $$ = $1 || $3; }
| NOT expr { $$ = ($2 == 0); }
| '(' expr ')' { $$ = $2; }
;

%%

// Additional C code
int yyerror (char *s) {
    fprintf (stderr, "%s\n", s);
}

int main() {
  yyparse();
  return 0;
}
