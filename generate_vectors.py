import math
import random
import Circular_Movement_Plotter
import weightedfreeroam


def generate_vectors(duration, actorlist, direction):
    # iterate through frames
    for i in range(duration):
        print(f"Frame - {i} of {duration}")
        offsetlist = []
        for Actor in actorlist:
            offset = (math.sqrt(((abs(Actor.vectors[i][0])) ** 2) + ((abs(Actor.vectors[i][1])) ** 2)))
            offsetlist.append(offset)

        av_offset = sum(offsetlist) / len(offsetlist)

        # iterate through actors
        for Actor in actorlist:
            # find intersection of circle around [0, 0] with movement circle
            offset = (math.sqrt(((abs(Actor.vectors[i][0])) ** 2) + ((abs(Actor.vectors[i][1])) ** 2)))
            intersections = Circular_Movement_Plotter.get_intersections(0, 0, offset, Actor.vectors[i][0],
                                                                        Actor.vectors[i][1], Actor.speed)

            # if no intersections, freeroam
            if intersections == None:
                lastmovement = [(Actor.vectors[i][0] - Actor.vectors[i - 1][0]),
                                (Actor.vectors[i][1] - Actor.vectors[i - 1][1])]
                movement = weightedfreeroam.weightedfreeroam(lastmovement, Actor.speed)

            # if intersection found, select the correct one based on direction of movement
            else:
                movement = Circular_Movement_Plotter.circular_movement(direction, intersections, Actor.vectors[i])

            # convert movement to new vectors
            newvectors = [Actor.vectors[i][0] + movement[0], Actor.vectors[i][1] + movement[1]]

            newvectors.append(Actor.vectors[i][2])

            # randomise new vector
            for j in range(len(newvectors)):
                weight = av_offset / offset

                if weight > 0:
                    upperlim = int(2 * weight)
                    lowerlim = -1

                elif weight < 0:
                    upperlim = 1
                    lowerlim = int(2 * weight)

                else:
                    upperlim = 2
                    lowerlim = -2

                if j == 2:
                    upperlim = 2
                    lowerlim = -2
                factor = random.randint(lowerlim, upperlim)

                newvectors[j] = newvectors[j] + factor

            Actor.vectors.append(newvectors)

    return actorlist