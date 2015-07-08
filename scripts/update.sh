#!/bin/bash

cd /home/digits/digits

echo Starting update.

# Save local edits
git stash

# Update from repository
git pull https://github.com/tdrimmelen/digits.git

echo Update executed. Restarting webserver.

(sleep 1 ; nohup sudo /etc/init.d/apache2 restart > /dev/null 2>&1) &

