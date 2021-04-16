''' This script extracts the coordinates from the header of an EMAN2 HDF image stack.

It assumes this stack was created using EMAN2 Boxer.

.. Created on Mar 27, 2014
.. codeauthor:: robertlanglois
'''

import sys
import EMAN2
import numpy

if __name__ == '__main__':
    
    stack = sys.argv[1]
    output = sys.argv[2]
    
    fout = open(output, 'w')
    for i in xrange(EMAN2.EMUtil.get_image_count(stack)):
        aimg = EMAN2.EMData()
        aimg.read_image(stack, i)
        coords=numpy.asarray(aimg['ptcl_source_coord'])
        fout.write("\t".join(["%d"%int(c*8) for c in coords])+"\n")
    fout.close()



