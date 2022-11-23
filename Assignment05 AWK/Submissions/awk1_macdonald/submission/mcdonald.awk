#!/usr/bin/awk -f

BEGIN{
    FS=":"
}
{
        printf("Old McDonald had a farm ei-ei-o\nOn that farm he had a %s ei-ei-o\nWith a %s-%s here, %s-%s there\nHere a %s there a %s, everywhere %s-%s\n",$1,$2,$2,$2,$2,$2,$2,$2,$2);
         

        #printf("%s %s",$1,$2)
        #curranimal=$1         # taking animal name that is before the colon
        #currsound=$2        # taking sound name that is after the colon

        #printf("%s \t %s",$curranimal,$currsound)

        #echo $curranimal
        #echo $currsound
        #{gsub(/animal/,curranimal)}1
        #sub(/animal/,$1) givenstr;
        #sub(/sound/,$2) givenstr;
        #"s/animal/$curranimal/g; s/sound/$currsound/g"

        #print givenstr;
        printf("\n");
}
END{
    printf("Old McDonald had a farm ei-ei-o");
}

