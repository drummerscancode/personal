#!/bin/sh

FILE=time.csv
TODAY=`date`
TIME=`date`

ALREADYLOGGEDINTODAY=`grep`

if [[ -z $ALREADYLOGGEDINTODAY]]; then 
	# It's a new day
	echo -n $TODAY $TIME > $FILe
else
	echo -n ";$TIME" >> $FILE
fi

