#!/bin/bash

if [ "$1" != "shotclock" ] && [ "$1"  != "scoreboard" ] ; then
	
	echo "Missing or unknown module"
	echo "usage: $0 [shotclock|scoreboard]"

	exit 1
fi

module=$1

wget https://raw.githubusercontent.com/tdrimmelen/digits/master/install/install1.sh
wget https://raw.githubusercontent.com/tdrimmelen/digits/master/install/install2.sh
wget https://raw.githubusercontent.com/tdrimmelen/digits/master/install/install3.sh
wget https://raw.githubusercontent.com/tdrimmelen/digits/master/install/update11-12.sh

chmod u+x *sh

./install1.sh
./install2.sh
./install3.sh ${module}
./update11-12.sh ${module}

echo "Finished install. Reboot Pi now (type reboot followed by enter)"
