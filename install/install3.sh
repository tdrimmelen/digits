#!/bin/bash

app=digits
module=schotklok

#If not docker than get code from GIT
if [ -z "$docker" ]; then

	sudo su - ${app} -c "git clone https://www.github.com/tdrimmelen/${app}"

fi 

ln -s /home/digits/digits/conf/${module}.conf /etc/apache2/sites-enabled/${module}.conf
a2enmod wsgi
a2dissite 000-default

mkdir /var/log/${app}
chown www-data:www-data /var/log/${app}
