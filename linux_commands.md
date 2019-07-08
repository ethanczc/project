# List of useful linux commands

__Find background tasks__

`ps -A`\
`ps aux`

__Find packages installed by pip__

`pip3 list`

__Find background running services__

`service --status-all`\
`systemctl list-units -t service`\
`systemctl list-units -t service -all`\
or target your service application\
`systemctl is-active "applicationName".service`\
`systemctl status "applicationName".service`

__Connect to wifi__

`sudo nano /etc/network/interfaces`\
Type in the following at the bottom
>auto wlan0\
>allow-hotplug wlan0\
>iface wlan0 inet dhcp\
>    wpa-ssid "SSID"\
>    wpa-psk "password"\

ctrl x, save and quit

__Change to static ip__

`ifconfig` - check the name of the ethernet port\
`sudo nano /etc/network/interfaces`\
Type in the following at the bottom
>auto "portName"\
>iface "portName" inet static\
>address "staticIp"\
>netmask 255.255.255.0

ctrl x, save and quit\
`sudo ifup "portName"`\
check if static ip is updated\
`hostname -I`

__Change default keyboard__

`sudo nano /etc/default/keyboard`

__Check os version__

`cat /etc/os-release`

__Locations of important stuffs__

errors/log/messages\
`/var/mail`\
`/var/log/messages`\
`/var/log/syslog`

pip packages\
`/usr/local/lib/python3.5/dist-packages`
