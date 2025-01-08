# Compare files App 
# This is a simple which let you compare two files to check they are same or not
# In this project we are using hashlib library to mange hash of file 

# Author Details 
# Name  :  Er. Amar kumar 
# Email :  amarkumar9685079691@gmail.com 

# Start of a source code

import hashlib


class CompareFileApp:
    _file1 = _file2 = None 

    def __init__(self, file1, file2):
        self._file1 = file1
        self._file2 = file2  

    def _getHashOfile(self, file):
        
        hash = hashlib.sha1()

        with open(file, 'rb') as fileObj:
            chunk = 0
            while chunk != b'':
               chunk = fileObj.read(1024)
               hash.update(chunk)   

        return hash.hexdigest()
     
    def compareFile(self):
        try:
            f1_hash = self._getHashOfile(self._file1)
            f2_hash = self._getHashOfile(self._file2)
         
            return f1_hash == f2_hash        
        except:
            print("App not working! Please try again")
            exit(0)


if __name__ == "__main__": 
        
    file1 = "file1.txt"
    file2 = "file2.txt"
    
    app = CompareFileApp(file1, file2)

    if app.compareFile():
       print("Files are same")
    else:
       print("File are not same")




# End of a source code