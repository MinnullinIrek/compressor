import tinify
from glob import glob
import os.path
tinify.key = "5Cv1jxynrBxCNGWFpwc4LpxNDT5PfNJd"
source_dir_name = 'D:/w4/nexters/src'
destination_dir_name = 'dist'

def isDirectory(fileName):
    return os.path.isdir(fileName)


def checkExt(file):
    filename, file_extension = os.path.splitext(file)
    print("ext of " + file + " is " + file_extension)
    return file_extension == '.png' or file_extension == '.jpg'

def compresFile(filename):
    return tinify.from_file(filename)

def replaceFile(source,  fullName):
    source.to_file(fullName)

def getAllFilesInDir(dir):
    print('directory: ' + dir)
    for innerFile in os.listdir(dir):
        if isDirectory(dir+'/'+innerFile):
            print('directory: ' + innerFile)
            getAllFilesInDir(dir+'/'+innerFile)
        else:
            print("not directory " + innerFile)
            if checkExt(innerFile):
                print("compressing " + innerFile)
                source = compresFile(dir+'/'+innerFile)
                replaceFile(source, dir+'/'+innerFile)
                print("compressed " +  dir+'/'+innerFile)

        
# get all files names in directory
files = glob(source_dir_name + '/*')
# compress all files

getAllFilesInDir(source_dir_name)

def second():
    for file in files:
        if os.path.isdir(file):
            print ("directory %s", file);



        print('compressing ' + file)
        source = tinify.from_file(file)
        file_name, ext = os.path.splitext(file)
        file_name = file_name.replace(source_dir_name + '/', '')
        source.to_file(destination_dir_name + "/" + file_name + ".png")
    print('compressed all images')
