import zipfile
import sys 
def ziper(a):
    z= zipfile.ZipFile(a,'w') 
    z.write(sys.argv[2])
    z.write(sys.argv[3])
    z.close()
ziper(sys.argv[1])     
