# main-e2.1
1 channel stage control\
2 channel irrigation\
2 channel LED\
1 channel dosing

# Hardware Requirements
1. Ubuntu Laptop/Desktop (LTS 16.04)
  * wx-python
  * mosquitto server
  * paho-mqtt
2. Raspberry pi 3B+ (Raspbian Stretch Lite)
  * serial
    * `sudo apt-get install python-serial`
  * mosquitto server
    * `sudo apt-get install mosquitto mosquitto-clients`
  * paho-mqtt
    * `sudo pip install paho-mqtt`
3. Arduino UNO R3
  * software serial

# Code
1. Ubuntu Laptop/Desktop
  * main-e2.1.py              (main code with GUI)
  * gui_main_e2_1.py          (GUI building block)
  * irrigation_recipe2.1.txt  (reference recipe)
2. Raspberry Pi 3B+
  * rpi_rack-1.0.py           (subscribe to topic RACK1)
  * rpi_rack_publish.py       (publish to topic RACK1S)
3. Arduino UNO R3
  * con_irrigation-s4.0.ino
  * con_led-s1.2.ino
  * con_doser-s2.0.ino
  
# Steps
1. set raspberry pi to login without password.
2. set raspberry pi to auto run python scripts at boot.
3. ensure ip address of host computer is 10.42.0.1, otherwise change the source code of
  * rpi_rack-1.0.py
  * rpi_rack_publish.py
4. ensure serial cables are plugged into raspberry pi in the correct sequence.
5. reboot raspberry pi.
6. run python main-e2.1.py

# Pre-requisites
1. install pip3\
`sudo apt-get install python3-pip`
2. install wxpython
