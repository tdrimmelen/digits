#!/bin/bash

app=digits

if [ -f /etc/apache2/sites-available/shotclock ]; then

        echo Shotclock config found
        module=shotclock

elif [ -f /etc/apache2/sites-available/scoreboard ]; then

        echo Scoreboard config found
        module=scoreboard

else

        echo No module found!!!
        exit 1
fi

a2dissite ${module}

rm /etc/apache2/sites-available/${module}

service apache2 stop

deluser --remove-home ${app}

echo Uninstall done!

