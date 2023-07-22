#python's os module and shutil allow us to easily navigate files 
#and directories on the computer and then perform actions on them, such as moving them or deleting them

#pwd is a special command in jupyter
f = open("practice.txt", "w")
f.write("This is a text file")
f.close()

#getcwd
import os
os.getcwd                                #get current working directory
print(os.listdir('C:\\Users'))


#shutil
#to move files around or to different locations
import shutil
shutil.move("practice.txt",'C:\\Users\\admin\\Desktop' )
print(os.listdir('C:\\Users\\admin\\Desktop'))

#deleting files
#os provides 3 methods to delete files

#os.unlink(path) which deletes a file at the path your provide
#os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
#shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path.

#All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file. 
#Instead we will use the send2trash module. A safer alternative that sends deleted files to the trash bin instead of permanent removal.


#to look folders, sub folders and files

'''''
for folder , sub_folders , files in os.walk("Example_Top_Level"):
    
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    
    print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')
'''''
    
    # Now look at subfolders