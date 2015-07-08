#!/bin/bash

cd /home/digits/digits

# Save local edits
git stash

# Update from repository
git pull https://github.com/tdrimmelen/digits.git
