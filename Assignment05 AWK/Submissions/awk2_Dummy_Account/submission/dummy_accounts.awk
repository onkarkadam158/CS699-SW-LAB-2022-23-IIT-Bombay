#!/usr/bin/awk -f 
{
	if ( $4 == "/bin/false" ) 
	{	print $1;
		if($1>max)
        {
			max=$1; 
        }
	}
}
END {print max;} 
	 



















