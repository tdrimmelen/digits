#!/bin/bash

app=digits
module=$1

echo "Start executing update scripts"

for file in /home/${app}/${app}/install/update.d/*; do

    echo "Start executing update script $file"
    [ -f "$file" ]  && source "$file" $module

done

echo "Finished executing update scripts"

