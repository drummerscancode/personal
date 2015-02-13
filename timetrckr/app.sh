#!/bin/sh

FILE=time.csv
TODAY=`date "+%Y-%m-%d"`
TIME=`date "+%H:%M:%S"`

ALREADYLOGGEDINTODAY=`grep $TODAY $FILE`

if [[ -z $ALREADYLOGGEDINTODAY ]]; then 
	# It's a new day, you look great today
	echo -n $TODAY $TIME > $FILE
else
	echo -n ";$TIME" >> $FILE
fi

