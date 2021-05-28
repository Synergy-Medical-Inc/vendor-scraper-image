import zipfile
import shutil
import urllib.request as request
from contextlib import closing
from keep_your_secrets import keep_your_secrets as kp



def synnex():
    with closing(request.urlopen(kp()[4])) as r:
        with open('/home/filestore/558671.zip', 'wb') as f:
            shutil.copyfileobj(r, f)

    with zipfile.ZipFile("/home/filestore/558671.zip","r") as zip_ref:
             zip_ref.extractall("/home/filestore")

def medplus_dwnld():
    with closing(request.urlopen(kp()[3])) as r:
        with open('/home/filestore/images.txt', 'wb') as f:
            shutil.copyfileobj(r, f)