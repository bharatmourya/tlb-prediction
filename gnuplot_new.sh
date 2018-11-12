gnuplot -p<<- EOF;
	set boxwidth 10
	set style fill solid

        set format y '%g' 
        set logscale y
        set key inside
        
        set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 ps 1.5   # --- blue
        set style line 2 lc rgb '#dd181f' lt 1 lw 2 pt 5 ps 1.5   # --- red

        #TLB shootdowns per second
        set title "TLB Shootdowns per second"
	set xlabel "time (seconds)"
	set ylabel "shootdown count (sum of all cores) - LOG scale"
        set term x11 0
        plot "with.gnu" with linespoints ls 2 title "with CPU AFFINITY set", \
             "without.gnu" with linespoints ls 1 title "without CPU AFFINITY set"
        
	pause -1
EOF
