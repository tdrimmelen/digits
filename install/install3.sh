#!/bin/bash

app=digits
module=$1
branch=$2

if [ -z "$docker" ]; then

	#If not docker than get code from GIT
	sudo su - ${app} -c "git clone https://www.github.com/tdrimmelen/${app}"
	sudo su - ${app} -c "cd ${app} ; git checkout ${branch}"
	sudo su - ${app} -c "git config --global user.email \"pi@noone.nowhere\""
	sudo su - ${app} -c "git config --global user.name \"Pi\""

	#Set some files needed wrt to hardware
	echo "dtparam=i2c1=on" >> /boot/config.txt
	echo "dtparam=i2c_arm=on" >> /boot/config.txt

	echo "i2c-dev" >> /etc/modules
fi 

ln -s /home/${app}/${app}/conf/${module}.conf /etc/apache2/sites-available/${module}.conf
a2enmod wsgi
a2dissite 000-default
a2ensite ${module}

mkdir /var/log/${app}
chown ${app}:${app} /var/log/${app}

cp -r /home/${app}/${app}/conf/sudoers.d/ /etc/
chmod 440 /etc/sudoers.d/*



