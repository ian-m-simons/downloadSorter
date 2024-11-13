import os
import platform


Path = ""
username = os.environ.get('USER', os.environ.get('USERNAME'))
if platform.system() == "Windows":
    Path = "C:\\Users\\"+username+"\\Downloads"

else:
    Path = "/home/"+username+"/Downloads"

downloadContents = os.listdir(Path)

for i in range(len(downloadContents)):
    extension = downloadContents[i].rsplit(".", 1)
    if (extension == ".png") or (extension == ".jpg"):
        if platform.system() == "Windows":
            
