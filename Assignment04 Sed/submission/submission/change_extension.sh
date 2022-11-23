#!/bin/bash


original_extension=$1
new_extension=$2

for itr in *;
do 
	filename=${itr%.*}
	ext=${itr##*.}
	if [[ $ext == $original_extension ]]; then
    
		mv $itr $filename.$new_extension		
	fi
done
