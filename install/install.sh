#!/bin/bash

if [ "$1" == "" ] ; then
	
	echo "Missing module"
	echo "usage: $0 <module name>"

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

