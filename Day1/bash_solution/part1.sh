#!/bin/bash

load_input() {
    awk '{print $1, $2}' "../inputs/$1"
}

calculate_distance() {
    paste <(sort -n <<< "$1") <(sort -n <<< "$2") | awk '{sum += ($1 - $2 > 0 ? $1 - $2 : $2 - $1)} END {print sum}'
}

col1=$(load_input "input" | cut -d' ' -f1)
col2=$(load_input "input" | cut -d' ' -f2)

total_distance=$(calculate_distance "$col1" "$col2")
echo "Distance: $total_distance"
