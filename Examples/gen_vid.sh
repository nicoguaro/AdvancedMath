#!/bin/bash
FNAME=$1
convert -delay 10 -loop 0 $FNAME*.png $FNAME.gif
rm -r $FNAME*.png
