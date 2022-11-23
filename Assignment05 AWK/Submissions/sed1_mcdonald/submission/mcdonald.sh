#!/bin/bash


givenstr="Old McDonald had a farm ei-ei-o\nOn that farm he had a animal ei-ei-o\nWith a sound-sound here, sound-sound there\nHere a sound there a sound, everywhere sound-sound\n"
tempstr=$givenstr

while read -r line
do
    input="$line"
    #echo $input
    curranimal=${input%:*}  # taking animal name that is before the colon
    currsound=${input##*:}        # taking sound name that is after the colon
    #echo $curranimal
    #echo "$currsound"
    echo -e "$tempstr" | sed "s/animal/$curranimal/g; s/sound/$currsound/g"
    tempstr=$givenstr

done < input.txt

echo "Old McDonald had a farm ei-ei-o"