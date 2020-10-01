#!/bin/bash

app=digits
module=$1


for file in /home/${app}/${app}/install/update.d/*; do

    [ -f "$file" ]  && source "$file" $module

done



