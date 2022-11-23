#!/usr/bin/awk -f 

{
	tempColumn = $2;
	$2 = $3;
	$3 =tempColumn;
	printf("%s %s %s %s\n", $1,$2,$3,$4);
}	 



















