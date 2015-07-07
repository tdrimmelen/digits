#!/bin/bash

app=digits

apt-get -y update

apt-get -y install  apache2 \
	python-bottle \
	python-setuptools \
	libapache2-mod-wsgi \
	sudo \
	net-tools \
	vim \
	git


adduser --disabled-password --gecos "" ${app}
sudo su - ${app} -c "git clone https://www.github.com/tdrimmelen/${app}"

ln -s /home/${app}/${app}/conf/${app}.conf /etc/apache2/sites-enabled/${app}.conf
a2enmod wsgi
a2dissite 000-default

mkdir /var/log/${app}
chown www-data:www-data /var/log/${app}
