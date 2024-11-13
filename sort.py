import os
import platform


print("success")
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
print(Paths)

downloadContents = os.listdir(Paths['Downloads'])
"""
for i in range(len(downloadContents)):
    extension = downloadContents[i].rsplit(".", 1)
    if (extension == ".png") or (extension == ".jpg"):
        if OperatingSystem == "Windows":
            
"""         
