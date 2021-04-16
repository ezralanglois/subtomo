#!/bin/bash


yum install -y curl which

EMAN2="http://blake.grid.bcm.edu/software/EMAN2/software_129/eman2.1.linux64.tar.gz"
curl -k -L ${EMAN2} -o eman2.1.linux64.tar.gz || true
tar -xzf eman2.1.linux64.tar.gz
mv EMAN2 /opt/

