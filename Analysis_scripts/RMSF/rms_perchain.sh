#!/bin/bash

COMMAND="parm ../../stripped_nosalt.parm7 \n"
COMMAND="$COMMAND trajin ../../nosalt-nowat.nc 43001 last\n" 
COMMAND="$COMMAND rms :2-19@C1,C2,C3,C4,O5,C5 \n"

i=2
until [ $i == 482 ]; 
do
        j=$(($i+17))
	COMMAND="$COMMAND atomicfluct rmsf_${i}_${j} out rmsf_${i}_${j}.dat :${i}-${j}@C*,O5 bymask \n"
        i=$(($i+20))
done



COMMAND="$COMMAND go"
echo -e "$COMMAND" | cpptraj

