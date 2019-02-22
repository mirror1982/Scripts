#!/bin/bash

echo -n "Enter start IP:  "
read st_ip
echo -n "Enter end IP:  "
read end_ip

for i in $(eval echo "{$st_ip..$end_ip}");
do
ping -c 1 192.168.5.$i;
done | egrep "PING|Unr"

