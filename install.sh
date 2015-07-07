#!/bin/bash

apt-get -y update

apt-get -y install  apache2 \
	python-bottle \
	python-setuptools \
	libapache2-mod-wsgi \
	sudo \
	net-tools \
	vim \
	git


adduser --disabled-password --gecos "" digits
sudo su - digits -c 'git clone https://www.github.com/tdrimmelen/digits'

ln -s /home/digits/digits/conf/schotklok.conf /etc/apache2/sites-enabled/schotklok.conf
a2enmod wsgi
a2dissite 000-default

