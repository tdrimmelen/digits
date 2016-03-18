#!/bin/bash

app=digits 
 
adduser --disabled-password --gecos "" ${app} 
usermod -a -G i2c ${app}

