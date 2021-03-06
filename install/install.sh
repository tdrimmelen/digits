#!/bin/bash

if [ "$1" != "shotclock" ] && \
   [ "$1"  != "shotclockcseries" ] && \
   [ "$1"  != "shotclockak30" ] && \
   [ "$1"  != "scoreboard" ] && \
   [ "$1"  != "scoreboardak30" ] && \
   [ "$1"  != "scoreboardledyears3505" ] && \
   [ "$1"  != "scoreboardledyears3510" ] && \
   [ "$1"  != "scoreboardwesterstrandbasic200250" ] \
   ; then
	
	echo "Missing or unknown module"
	echo "usage: install.sh [shotclock|shotclockcseries|shotclockak30|scoreboard|scoreboardak30|scoreboardledyears3505|scoreboardledyears3510|scoreboardwesterstrandbasic200250]"

	exit 1
fi

module=$1
basemodule=$1

if [ "$1"  == "shotclockcseries" ] || [ "$1"  == "shotclockak30" ] ; then

	basemodule="shotclock"
	module="shotclockak30cseries"

fi

if [ "$1"  == "scoreboardak30" ] || \
   [ "$1"  == "scoreboardledyears3505" ] || \
   [ "$1"  == "scoreboardledyears3510" ] || \
   [ "$1"  == "scoreboardwesterstrandbasic200250" ] \
   ; then

	basemodule="scoreboard"

fi

branch=master

if [ "$2" != "" ] ; then

	echo "Using github branch $2"
	branch=$2

fi

wget https://raw.githubusercontent.com/tdrimmelen/digits/${branch}/install/install1.sh
wget https://raw.githubusercontent.com/tdrimmelen/digits/${branch}/install/install2.sh
wget https://raw.githubusercontent.com/tdrimmelen/digits/${branch}/install/install3.sh
wget https://raw.githubusercontent.com/tdrimmelen/digits/${branch}/install/install4.sh

chmod u+x *sh

./install1.sh
./install2.sh
./install3.sh ${basemodule} ${branch}
./install4.sh ${module}

echo "Finished install. Reboot Pi now (type reboot followed by enter)"
echo "Installed with parameters ${basemodule} ${module} ${branch}"
