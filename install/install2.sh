#!/bin/bash

app=digits 
module=schotklok 
 
adduser --disabled-password --gecos "" ${app} 
usermod -a -G i2c www-data 

