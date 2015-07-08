#!/bin/bash

cd /home/digits/digits

if [ "$1" = "on" ] ; then
	link=IOPiStub		
else 
	if [ "$1" = "off" ] ; then
		link=IOPiReal
	else
		echo "Usage: $0 [on|off]"
		exit 1
	fi
fi

rm IOPi
ln -s ${link} IOPi
