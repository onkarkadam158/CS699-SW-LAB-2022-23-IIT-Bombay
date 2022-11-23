mkdir demo
cd demo
mkdir code
mkdir doc
cd code
PROG=hello.c
cp ../../$PROG ./
gcc -o hello $PROG
./hello
