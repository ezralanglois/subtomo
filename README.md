# subtomo
Legacy scripts for doing subtomogrphic analysis


## Running

docker run --rm docker.io/ezralanglois/subtomo -c "import EMAN2"

### You need to mount the directory with the data in the docker container

 - `$HOME/Downloads` is the local directory that contains the HDF files
 - /opt/scripts/sta_extract_coords.py is the script that extracts coordinates from the HDF file


    docker run -v$HOME/Downloads:/data --rm docker.io/ezralanglois/subtomo /opt/scripts/sta_extract_coords.py /data/INS_HG_22_g1_t3_noglucose_bound.hdf /data/INS_HG_22_g1_t3_noglucose_bound.csv