#!/bin/sh
### BEGIN INIT INFO
# Provides:          noip
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Simple script to start a program at boot
### END INIT INFO

sleep 30
sudo modprobe bcm2835-v4l2
source ~/.profile
workon cvpy2
cd myversion-smart-security-cam/
python main.py

exit 0
