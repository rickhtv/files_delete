##Program to delete all the files inside a specific directory

#Imports 
import os 
import glob 

#Folder Directory
os.chdir("C:/...") #Directory to delete the specific files 

extension = 'xlsx' #Inform the extension to delete a specific type of file 
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
for i in range(0,len(all_filenames)):
    os.remove(all_filenames[i])