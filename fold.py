import os
import shutil


path_input="C:\\Users\\Michele\\Desktop"
path_output="C:\\Users\\Michele\\Desktop\\immagini"
files = os.listdir(path_input+'/lfw')
for folder in files:
    for image in os.listdir(path_input+'/lfw/'+folder):
        print(path_input+'/lfw/'+folder+'/'+image)
        shutil.move(path_input+'/lfw/'+folder+'/'+image, path_output)

