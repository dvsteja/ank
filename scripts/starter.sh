#!/bin/sh

# rm -f nohup.out
# nohup tcpdump -i eth0 -nn tcp -w inputs/input-tcpdump.txt &

tcpdump -i eth0 -Z root -nn tcp >> onlo_fl_n_0.txt &
# Write tcpdump's PID to a file
echo $! > /var/run/tcpdump.pid

netstat -npt -c >> onlo_fl_n.txt &
echo $! > /var/run/netstat.pid