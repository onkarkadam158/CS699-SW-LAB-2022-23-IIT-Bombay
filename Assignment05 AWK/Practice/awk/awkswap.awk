#!/usr/bin/awk -f 

{
	temp = $2;
	$2 = $3;
	$3 =temp;
	printf("%s %s %s %s\n", $1,$2,$3,$4);
}	 




















