#!/bin/bash



directory=$1

	#echo "$directory"

if [[ -z $directory ]]; then
	echo "Usage: photo-rename.sh path"
	exit 1
else
	if  [[ ! -d $directory ]]; then
		echo "Directory does not exist."
		exit 2
	fi
fi

mkdir output
	
for itr in $1/* ;
do 

	#fullname=${itr%*.}
	filename=$(basename $itr)
	#filename=${fullfilename%.*}
	#echo "File name: $filename"
	ext=${filename##*.}
	#echo "extension $ext"
	size=${#filename}

	if [[ "$ext" == "jpg" && "$size" -gt 11 ]]  ; then

		str=${filename:0:8}
		echo "str is $str"
		if [[ "$str" =~ ^[0-9]{8}*$ ]]; then
		
			#echo "Entering 2nd if and str is $str"
			dd=${filename:0:2}
			mm=${filename:2:2}
			yy=${filename:4:4}
			any=${filename:8:${#filename}}
			
			#echo "$filename"
			#echo "$ext"
			#echo "$size"
			
			newfilename=$yy-$mm-$dd-$any
			
			#echo "Itr = $itr"
			echo "final copying $filename to New name $newfilename"
			cp "$filename" output/"$newfilename" 
		fi
		 
		
	fi
done


: '
counter=0
		echo "counter $counter"
		for c in $filename ;
		do
			counter=$(( counter+1 ))
			echo "$counter"
			echo "$c"
			if [ $counter -eq 9 ]; then
				break
			fi
			
			if [ $((c)) == 0 -o $((c)) == 1 -o $((c)) == 2 -o $((c)) == 3 -o $((c)) == 4 -o $((c)) == 5 -o $((c)) == 6 -o $((c)) == 7 -o $((c)) == 8 -o $((c)) == 9 ]; then
				echo "true"
			else
				flag=1
				break
			fi
							
		done
		'
