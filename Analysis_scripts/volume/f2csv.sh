#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 input_file.txt output_file.csv"
    exit 1
fi

input_file="$1"
output_file="$2"

sed 's/ \{1,\}/,/g' "$input_file" > "$output_file"

echo "Conversion complete: $output_file"

