#!/bin/sh

FILE=time.csv
TODAY=`date "+%Y-%m-%d"`
TIME=`date "+%H:%M:%S"`

[ ! -f $FILE ] && echo "File $FILE not found!\n Creating it now!" && touch $FILE

ALREADYLOGGEDINTODAY=`grep $TODAY $FILE`

if [ -z "$ALREADYLOGGEDINTODAY" ]; then 
        # It's a new day, you look great today
        printf "%s %s;" "$TODAY" "$TIME" > $FILE
else
		# print only the time
        printf "%s;" "$TIME" >> $FILE
fi
