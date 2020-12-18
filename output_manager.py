import os

def print_files(vectors, angles):

    newpath = 'vectors'

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    data = 'vectors'
    actoroutput = ('{}\\prey1{}.txt'.format(newpath, data))


    with open(actoroutput, 'a')as file_object:

        for i in vectors:
            for e in range(0, 3):
                file_object.write(str(i[e]))
                if e != 2:
                    file_object.write(",")
            file_object.write("\n")


    data = 'angles'
    actoroutput = ('{}\\prey1{}.txt'.format(newpath, data))


    with open(actoroutput, 'a')as file_object:
        for i in angles:
            for e in range(0, 3):
                file_object.write(str(i[e]))
                if e != 2:
                    file_object.write(",")
            file_object.write("\n")


