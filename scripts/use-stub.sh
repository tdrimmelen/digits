#!/bin/bash

cd /home/digits/digits

echo $0 called with param $1

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
echo "ln -s ${link} IOPi executed"

(sleep 1 ; nohup sudo /etc/init.d/apache2 restart > /dev/null 2>&1) &

exit 0
