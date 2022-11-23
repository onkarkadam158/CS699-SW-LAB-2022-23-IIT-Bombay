#!/bin/bash

# This script must take a single argument, a file input.  It must run
# the script marks-count.awk on that input, and use the output to extract
# the lines corresponding to the three students with the maximum
# negative (magnitude wise) house points.

# You need not check that a single argument is given, you can assume
# that a single argument will be given.

# Marks: 4
# 2 marks for correctness
# 2 marks for single line solution (can use pipes, but no multiple
# bash statements)

# START

 awk -f que3.awk $1 | sort -t, -n -k5 | head -n 3

# END
