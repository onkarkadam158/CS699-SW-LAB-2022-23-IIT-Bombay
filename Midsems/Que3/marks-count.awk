#!/usr/bin/awk -f

# This awk script is to be run as awk -f marks-count.awk
# It takes as input a CSV file, whose:
# first column is student roll number
# second column is student name
# third column is student hostel name

# fourth column onwards is the marks obtained in in-class quizzes
# (like the SAFE quizzes we have in this course) on various days
# You can assume (need not check) that each mark entry is either an
# empty string, or an integer

# The first row is a header row (which you can ignore in the script)

# You can assume that the input has at least four columns, but you
# CANNOT assume any specific value for the number of columns in the
# input

# The output of the script must be in CSV format (comma separated, not
# tab separated).  The output must be:
# first column: student roll number
# second column: student name
# third column: student hostel name
# fourth column: sum of all the positive marks obtained by that student
# fifth column: sum of all the negative marks obtained by that student
# sixth column: number of zero marks obtained by that student (DO NOT count empty strings as zero marks)
# There should not be any header row in the output

# Marks: 5 marks

# START
BEGIN{
FS=",";
}
{
sumpos=0;
sumneg=0;
cntz=0;
for(i=4;i<=NF;i++)
{
    if( $i == "" )
    	{continue;}
    if( $i == 0 )
    	{cntz++;}
    if( $i < 0 )
    	{sumneg=sumneg+$i;}
    if( $i > 0)
    	{sumpos=sumpos+$i;}
}

if( NR != 1 && NF > 3)
{
	printf("%s,%s,%s,%d,%d,%d\n",$1,$2,$3,sumpos,sumneg,cntz);
}
}


# END
