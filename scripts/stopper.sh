#!/bin/sh
if [ -f /var/run/tcpdump.pid ]
then
        kill `cat /var/run/tcpdump.pid`
        rm -f /var/run/tcpdump.pid
fi

if [ -f /var/run/netstat.pid ]
then
        kill `cat /var/run/netstat.pid`
        rm -f /var/run/netstat.pid
fi