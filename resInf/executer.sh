#!/bin/bash
for i in `seq 1 245`;
do
  start=$(cat inicio.txt)
  end=$(cat final.txt)
  sep="-"
  ext=".csv"
  python2 Exporter.py --since $start --until $end --querysearch 'influenza' --maxtweets 3000
  python dateChange.py
  echo $start$sep$end$ext
done
