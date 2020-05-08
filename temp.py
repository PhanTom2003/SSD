import os 
import urllib.request
import tarfile 
import zipfile


data_dir="./data"
if not os.path.exists(data_dir):
    os.mkdir(data_dir)
    
url="http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar"
target_dir=os.path.join(data_dir,"VOCtrainval_11-May-2012.tar")
if not os.path.exists(data_dir):
    urllib.request.urlretrieve(url,target_dir)
    tar = tarfile.TarFile(target_dir)
    tar.extractall(data_dir)
    tar.close
