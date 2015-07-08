#!/bin/bash

if [ "$1" != "shotclock" ] && [ "$1"  != "timeclock" ] ; then
	
	echo "Missing or unknown module"
	echo "usage: $0 [shotclock|timeclock]"

	exit 1
fi

module=$1

wget https://raw.githubusercontent.com/tdrimmelen/digits/master/install/install1.sh
wget https://raw.githubusercontent.com/tdrimmelen/digits/master/install/install2.sh
wget https://raw.githubusercontent.com/tdrimmelen/digits/master/install/install3.sh

chmod u+x *sh

./install1.sh
./install2.sh
./install3.sh ${module}

