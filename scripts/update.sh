#!/bin/bash

app=digits

cd /home/digits/digits

echo Starting update.

# Save local edits
sudo su - ${app} -c "git stash"

# Update from repository
sudo su - ${app} -c "git pull"

# Run update script
source install/update.sh

echo Update executed. Restarting webserver.

(sleep 1 ; nohup sudo /etc/init.d/apache2 restart > /dev/null 2>&1) &

