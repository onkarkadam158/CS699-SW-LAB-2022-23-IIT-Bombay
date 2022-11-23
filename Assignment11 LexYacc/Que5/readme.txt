//run the code with following commands
lex calc.l
yacc calc.y -d
cc lex.yy.c calc.tab.c -ll
./a.out < input.txt > temp.txt //this will give input.txt as a input to ./a.out and redirect the output to temp.txt file 

//compare your terminal output with the content of answer.txt
diff temp.txt answer.txt

//here we assumed the operator will have space before and after

