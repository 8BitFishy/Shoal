import os

def clearfiles():

    for files in os.walk("vectors"):
        filelist = list(files[2])
        for file in filelist:
            if "prey" in file:
                dir = os.path.join("vectors/", file)
                os.remove(dir)