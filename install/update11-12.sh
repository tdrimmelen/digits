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
	chmod u+w /home/${app}/${app}/digits.cfg

fi


