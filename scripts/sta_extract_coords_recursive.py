''' This script extracts the coordinates from the header of an EMAN2 HDF image stack.

It assumes this stack was created using EMAN2 Boxer.

.. Created on Mar 27, 2014
.. codeauthor:: robertlanglois
'''

import sys
import EMAN2
import numpy
import os

if __name__ == '__main__':
    
    stack_dir = sys.argv[1]
    output_dir = sys.argv[2]

    print("Stack directory {}".format(stack_dir))
    for root, _, files in os.walk(stack_dir):
        files = [fi for fi in files if fi.endswith(".hdf")]
        print("Processing {} files in {}".format(len(files), root))
        for hdf_file in files:
            stack = os.path.join(root, hdf_file)
            output = os.path.join(output_dir, os.path.splitext(os.path.basename(hdf_file))[0]+".csv")
            try:
                count = EMAN2.EMUtil.get_image_count(stack)
            except:
                print("Skipping: {}".format(stack))
                continue
            fout = open(output, 'w')
            for i in xrange(count):
                aimg = EMAN2.EMData()
                aimg.read_image(stack, i)
                coords=numpy.asarray(aimg['ptcl_source_coord'])
                fout.write("\t".join(["%d"%int(c*8) for c in coords])+"\n")
            fout.close()




