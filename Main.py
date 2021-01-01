import random
import angle_generator
import output_manager
import clear_files
import Generate_Actors
import generate_vectors

duration = 500
rotations = 0
angle = 0

clear_files.clearfiles()
actorlist = []
actorcount = 500
direction = "anti-clockwise"



if __name__ == "__main__":

    #initialise actors
    #generate actor list
    actorlist = Generate_Actors.Generate_Actors(actorcount)
    #assign actor traits
    #assign actor starting vectors

    print("\n\n------------------------------Generating Vectors------------------------------\n\n")
    actorlist = generate_vectors.generate_vectors(duration, actorlist, direction)

    print("\n\n------------------------------Generating Angles------------------------------\n\n")
    actorlist = angle_generator.angle_generator(duration, actorlist)


output_manager.print_files(actorlist)