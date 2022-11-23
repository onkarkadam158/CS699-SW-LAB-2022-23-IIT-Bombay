mkdir output

original_extension="jpg"
new_extension="png"

for itr in * ;
do 
	filename=${itr%.*}
	ext=${itr##*.}
	if [ "$ext" == "$original_extension" ] ; then
		mv $itr output/$filename.$new_extension		
	fi
done


