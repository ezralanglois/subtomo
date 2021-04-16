#!/master.raid/home_master/robertl/EMAN2/Python-2.7-ucs4/bin/python
'''
.. Created on Apr 2, 2014
.. codeauthor:: robertlanglois
'''
import sys
import EMAN2
import numpy

if __name__ == '__main__':
    
    stack = sys.argv[1]
    aimg = EMAN2.EMData()
    aimg.read_image(stack, 0, True)
    
    header = aimg.get_attr_dict()
    print header
    print header['nx']
    print header['ny']
    print header['nz']
    if 'ptcl_source_coord' in header: print header['ptcl_source_coord']
