#!/bin/bash

app=digits

if [ -f /etc/apache2/sites-available/shotclock ]; then

        echo Shotclock config found
        module=shotclock

elif [ -f /etc/apache2/sites-available/scoreboard ]; then

        echo Scoreboard config found
        module=scoreboard

else

        echo No moudle found!!!
        exit 1
fi

a2ensite ${module}

rm /etc/apache2/sites-available/${module}

deluser --remove-home ${app}

echo Uninstall done!

