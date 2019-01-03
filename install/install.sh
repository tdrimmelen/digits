#!/bin/bash

if [ "$1" != "shotclock" ] && \
   [ "$1"  != "shotclockC4" ] && \
   [ "$1"  != "scoreboard" ] && \
   ; then
	
	echo "Missing or unknown module"
	echo "usage: $0 [shotclock|shotclockC4|scoreboard]"

	exit 1
fi

module=$1
basemodule=$1

if [ "$1"  == "shotclockC4" ] ; then

	basemodule="shotclock"

fi

branch=master

if [ "$2" != "" ] ; then

	echo "Using github branch $2"
	branch=$2

fi

wget https://raw.githubusercontent.com/tdrimmelen/digits/${branch}/install/install1.sh
wget https://raw.githubusercontent.com/tdrimmelen/digits/${branch}/install/install2.sh
wget https://raw.githubusercontent.com/tdrimmelen/digits/${branch}/install/install3.sh
wget https://raw.githubusercontent.com/tdrimmelen/digits/${branch}/install/update11-12.sh

chmod u+x *sh

./install1.sh
./install2.sh
./install3.sh ${basemodule} ${branch}
./update11-12.sh ${module}

echo "Finished install. Reboot Pi now (type reboot followed by enter)"
