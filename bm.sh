#!/bin/bash

echo > /sys/kernel/debug/tracing/trace
echo 1 > /sys/kernel/debug/tracing/events/tlb/enable
echo 1 > /sys/kernel/debug/tracing/tracing_on
#echo > trace1198
#echo > trace1199
#echo > trace1200
#strace -tt -fp 1198 -o trace1198&
#strace -tt -fp 1199 -o trace1199&
#strace -tt -fp 1200 -o trace1200&
../tracing/wrk/./wrk -t6 -c400 http://127.0.0.1/
echo 0 > /sys/kernel/debug/tracing/tracing_on
pkill strace
cp /sys/kernel/debug/tracing/trace /home/bharath/Desktop/remote1
cat /home/bharath/Desktop/remote1 | grep remote > remote2
#cat trace1198 | grep unmap > unmap1198
#cat trace1199 | grep unmap > unmap1199
#cat trace1200 | grep unmap > unmap1200
