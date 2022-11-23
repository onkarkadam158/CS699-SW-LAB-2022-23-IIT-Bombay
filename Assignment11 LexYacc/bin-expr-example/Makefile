bin-expr: bin-expr.c bin-expr.tab.c
	gcc -o bin-expr bin-expr.c bin-expr.tab.c -ll -ly

bin-expr.c: bin-expr.l bin-expr.tab.h
	flex -t bin-expr.l > bin-expr.c

bin-expr.tab.h bin-expr.tab.c: bin-expr.y
	bison -d bin-expr.y
