''' Place within the full tomogram a subtomogram average in the original position 
and orientation for each of the original subtomograms making up the average

Download to edit and run: :download:`sta_place_average.py <../../arachnid/snippets/sta_place_average.py>`

To run:

.. sourcecode:: sh
    
    $ python sta_place_average.py

.. note::
    
    Requires EMAN2 2.1

.. literalinclude:: ../../arachnid/snippets/sta_place_average.py
   :language: python
   :lines: 23-
   :linenos:

.. codeauthor:: Robert Langlois <rl2528@columbia.edu>
'''
import sys
import EMAN2
import numpy
#import os

if __name__ == '__main__':

    # Parameters
    tomogram = sys.argv[1]      # Decimated tomogram - 8 times
    alignment = sys.argv[2]     # Undecimated alignment parameters from EMAN2 e2spt_classaverage.py
    orig_stack = sys.argv[3]    # Undecimated volumes extracted with EMAN2 e2spt_boxer.py
    output = sys.argv[4]        # Output placement sans tomogram
    average = sys.argv[5]    # Undecimated volumes extracted with EMAN2 e2spt_boxer.py
    mask_file = sys.argv[6] if len(sys.argv)>6 else None
    bin_factor = 8
    
    tomo = EMAN2.EMData()
    tomo.read_image(tomogram)
    fulltomo = tomo.copy()
    tomo.to_zero()
    
    aligndict = EMAN2.js_open_dict(alignment) # @UndefinedVariable
    coords={}
    for key in aligndict.keys():
        off = key.find('_')+1
        id = int(key[off:])
        oem = EMAN2.EMData()
        oem.read_image(orig_stack, id)
        coords[id]=numpy.asarray(oem['ptcl_source_coord'])/8
    
    print "Tomogram dimensions", tomo.get_xsize(), tomo.get_ysize(), tomo.get_zsize()
    avg = EMAN2.EMData()
    avg.read_image(average)
    nx = avg.get_xsize()/bin_factor
    ny = avg.get_ysize()/bin_factor
    nz = avg.get_zsize()/bin_factor
        
    if mask_file is not None:
        emmask = EMAN2.EMData()
        emmask.read_image(mask_file)
        emmask = emmask.process('math.fft.resample', dict(n=bin_factor))
        npmask = EMAN2.EMNumPy.em2numpy(emmask)
        print npmask.max(), npmask.min(), npmask.sum(), numpy.prod(npmask.shape), (npmask==0).sum(), (npmask==1).sum()
        mask = numpy.nonzero(npmask>0.99999)
        nptomo = EMAN2.EMNumPy.em2numpy(tomo)
    else:
        mask = None
        
    
    print 'Place', len(aligndict), 'subtomos'
    for key in aligndict.keys():
        off = key.find('_')+1
        id = int(key[off:])
        trans = aligndict[key][0]
        cavg = avg.copy()
        itrans = trans.inverse()
        cavg.process_inplace("xform",{"transform":itrans})
        cavg = cavg.process('math.fft.resample', dict(n=bin_factor))
        x,y,z = coords[id]
        x = (2*int(x) - nx)/2
        y = (2*int(y) - ny)/2
        z = (2*int(z) - nz)/2
        if mask is not None:
            cmask = emmask.copy()
            sx,sy,sz = itrans.get_trans()
            itrans.set_trans((sx/bin_factor, sy/bin_factor, sz/bin_factor))
            cmask.process_inplace("xform",{"transform":itrans})
            npmask = EMAN2.EMNumPy.em2numpy(cmask)
            mask = numpy.nonzero(npmask>0.5)
            if id==0: print 'cavg', cavg.get_xsize()
            npcavg = EMAN2.EMNumPy.em2numpy(cavg)
            #print z,z+nz, y,y+ny, x,x+nx
            npsubset = nptomo[z:z+nz, y:y+ny, x:x+nx]
            npsubset[mask] = npcavg[mask]
        else:
            assert(False)
            tomo.insert_clip(cavg, (x, y, z))
    
    print 'done:', output
    tomo.write_image(output)

        
        
    
    
