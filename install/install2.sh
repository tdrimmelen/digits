#!/bin/bash

app=digits 
module=shotclock
 
adduser --disabled-password --gecos "" ${app} 
usermod -a -G i2c ${app}

