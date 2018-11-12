# tlb-prediction
script.sh contain script for collecting trace from and /sys/kernel/debug/trace

graphs:

python plot-ipi.py 'name' 'interval-10/100'
python plot-ipi-cdf.py 'name' 'interval-10/100'

store graphs in graphs folder

Till now no spikes observed in graphs
