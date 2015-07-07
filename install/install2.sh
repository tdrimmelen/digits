#!/bin/bash

app=digits


adduser --disabled-password --gecos "" ${app}

#If not docker than get code from GIT
if [ -z "$docker" ]; then

	sudo su - ${app} -c "git clone https://www.github.com/tdrimmelen/${app}"

fi 

ln -s /home/${app}/${app}/conf/${app}.conf /etc/apache2/sites-enabled/${app}.conf
a2enmod wsgi
a2dissite 000-default

mkdir /var/log/${app}
chown www-data:www-data /var/log/${app}
