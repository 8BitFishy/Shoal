import os

def print_files(actorlist):

    newpath = 'vectors'

    if not os.path.exists(newpath):
        os.makedirs(newpath)


    for Actor in actorlist:
        data = 'vectors'
        actoroutput = ('{}\\prey{}{}.txt'.format(newpath, Actor.id, data))


        with open(actoroutput, 'a')as file_object:

            for i in Actor.vectors:
                for e in range(0, 3):
                    file_object.write(str(i[e]))
                    if e != 2:
                        file_object.write(",")
                file_object.write("\n")


        data = 'angles'
        actoroutput = ('{}\\prey{}{}.txt'.format(newpath, Actor.id, data))


        with open(actoroutput, 'a')as file_object:
            for i in Actor.angles:
                for e in range(0, 3):
                    file_object.write(str(i[e]))
                    if e != 2:
                        file_object.write(",")
                file_object.write("\n")
