#!/bin/bash

app=digits
module=$1


if [ ! -f /home/${app}/${app}/logger.cfg ]; then

	echo "Installing logger.cfg"
	cp /home/${app}/${app}/conf/logger_tmpl.cfg /home/${app}/${app}/logger.cfg
	chmod u+w /home/${app}/${app}/logger.cfg

fi

if [ ! -f /home/${app}/${app}/digits.cfg ]; then

	echo "Installing digits.cfg"
	cp /home/${app}/${app}/conf/digits_tmpl.cfg /home/${app}/${app}/digits.cfg

	#Determine module names
	case $module in
		shotclock)
			var1="shotclock"
			var2=""
			var3=""
			;;
		shotclockak30cseries)
			var1="shotclockak30cseries"
			var2=""
			var3=""
			;;
		scoreboard)
			var1=""
			var2="timeclock"
			var3="scoreboard"
			;;
		scoreboardak30)
			var1=""
			var2=""
			var3="scoreboardak30"
			;;
		scoreboardledyears3505)
			var1=""
			var2=""
			var3="scoreboardledyears3505"
			;;
		scoreboardledyears3510)
			var1=""
			var2=""
			var3="scoreboardledyears3510"
			;;
		scoreboardwesterstrandbasic200250)
			var1=""
			var2=""
			var3="scoreboardwesterstrandbasic200250"
			;;
	esac

	#Write module names to config file
	mv /home/${app}/${app}/digits.cfg /home/${app}/${app}/digits.cfg.old

	cat /home/${app}/${app}/digits.cfg.old | \
	sed "s/####1/${var1}/g" | \
	sed "s/####2/${var2}/g" | \
	sed "s/####3/${var3}/g" > /home/${app}/${app}/digits.cfg

	chmod u+w /home/${app}/${app}/digits.cfg
fi