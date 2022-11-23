# For each of the 3 files marksX.csv (X=1,2,3), we want to generate
# marksX.top3neg as the output of running the script top3-neg.sh .
# Capture this dependence in a Makefile. The Makefile should capture
# the dependence across the relevant scripts as well as the
# input/output files.

# The default target of the Makefile should be the 3 output files
# marksX.top3neg (X=1,2,3)
all: top3-neg

marks-count: marks-count.awk marks1.csv marks2.csv marks3.csv
	awk -f marks-count.awk marks1.csv awk -f marks-count.awk marks2.csv awk -f marks-count.awk marks3.csv

top3-neg: marks-count
	bash top3-neg.sh marks-count

.PHONY: clean
clean:
	rm -f top3.neg 