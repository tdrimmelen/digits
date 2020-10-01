#!/bin/bash

apt-get -y update

apt-get -y install  apache2 \
	python-bottle \
	python-setuptools \
	libapache2-mod-wsgi \
	sudo \
	net-tools \
	vim \
	git \
	zip \
	python-smbus \
	python-pip

pip install pyserial



