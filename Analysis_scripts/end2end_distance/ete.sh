#!/bin/bash

COMMAND="parm ../../stripped_nosalt.parm7 \n"
COMMAND="$COMMAND trajin ../../nosalt-nowat.nc\n"

i=1

until [ $i == 481 ]; 
do
j=$(($i+19))
COMMAND="$COMMAND distance ${i}_${j}_dist :${i}@O4 :${j}@O1 out ete_fib.dat noimage \n"
i=$(($i+20))
done

COMMAND="$COMMAND go"
echo -e "$COMMAND" | cpptraj

