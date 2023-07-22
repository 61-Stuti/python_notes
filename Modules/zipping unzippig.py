f = open('fileone.txt', 'w+')
f.write('fileone')
f.close()

f = open('practice.txt', 'w+')
f.write('file2')
f.close()


import zipfile
comp_file = zipfile.ZipFile('comp_file.zip','w')     #create a zip file
comp_file.write('fileone.txt', compress_type = zipfile.ZIP_DEFLATED)               #compress the zip file
comp_file.write('practice.txt', compress_type = zipfile.ZIP_DEFLATED)               #add files to it
comp_file.close()

#unzipping
import shutil

shutil.unpack_archive('unzip_me_for_instructions.zip','','zip')
