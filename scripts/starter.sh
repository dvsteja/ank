#!/bin/sh
pip install -r requirements.txt
tcpdump -i eth0 -Z root -nn tcp >> onlo_fl_n_0.txt &
echo $! > /var/run/tcpdump.pid
netstat -npt -c >> onlo_fl_n.txt &
echo $! > /var/run/netstat.pid
python3 executor.py