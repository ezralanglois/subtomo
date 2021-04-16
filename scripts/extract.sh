#!/bin/bash

# This script requires EMAN2.1 to be installed

# Example running the script
# sh extract.sh INS_HG_22_g1_t1_noglucose_free.hdf INS_HG_22_g1_t1_noglucose.rec


coords=$1
tomo=$2
base=`dirname $0`

#${EMAN2DIR}/Python-2.7-ucs4/bin/
python ${base}/sta_extract_coords.py $coords ${coords}.tsv

e2spt_boxer.py $tomo --path . --boxsize 200 --output stacks/${coords##*/} --invert --coords ${coords}.tsv --normproc=normalize.mask  --masknorm=mask.sharp:outer_radius=80


