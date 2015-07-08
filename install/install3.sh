#!/bin/bash

app=digits
module=$1

#If not docker than get code from GIT
if [ -z "$docker" ]; then

	sudo su - ${app} -c "git clone https://www.github.com/tdrimmelen/${app}"
	sudo su - ${app} -c "git config --global user.email \"pi@noone.nowhere\""
	sudo su - ${app} -c "git config --global user.name \"Pi\""

fi 

ln -s /home/${app}/${app}/conf/${module} /etc/apache2/sites-available/${module}
a2enmod wsgi
a2dissite 000-default
a2ensite ${module}

mkdir /var/log/${app}
chown ${app}:${app} /var/log/${app}

cp -r /home/${app}/${app}/conf/sudoers.d/ /etc/
chmod 440 /etc/sudoers.d/*
