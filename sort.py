import os
import platform
import shutil

Paths = {"Downloads":"", "Documents":"", "Pictures":"", "Music":"", "Videos":""}
PathList = list(Paths.keys())
OperatingSystem = platform.system()
username = os.environ.get('USER', os.environ.get('USERNAME'))
if OperatingSystem == "Windows":
    tempPath = os.path.join("C:/Users/"+username) 
    for i in range(len(PathList)):
        Paths[PathList[i]]= tempPath + "/" + PathList[i]
        

else:
    tempPath = "/home/"+username
    for i in range(len(PathList)):
        Paths[PathList[i]] = tempPath + "/"+ PathList[i]

downloadContents = os.listdir(Paths['Downloads'])

for i in range(len(downloadContents)):
    extension = downloadContents[i].rsplit(".", 1)
    if (extension == "png") or (extension == "jpg") or (extension == 'jpeg') or (extension == 'gif'):
        shutil.move(Paths['Downloads']+"/"+downloadContents[i], Paths['Pictures']+"/"+downloadContents[i])
    if (extension == "mp4") or (extension == "mov") or (extension == 'avi)'):
        shutil.move(Paths['Downloads']+"/"+downloadContents[i], Paths['Videos']+"/"+downloadContents[i])
    if (extension == 'mp3') or (extension == 'wav'):
        shutil.move(Paths['Downloads']+"/"+downloadContents[i], Paths['Music']+"/"+downloadContents[i])
    else:
        shutil.move(Paths['Downloads']+"/"+downloadContents[i], Paths['Documents']+"/"+downloadContents[i])
