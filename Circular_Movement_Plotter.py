import math


def circular_movement(direction, intersections, vectors):
    movement = [0, 0]
    if direction == "anti-clockwise":

        if vectors[0] > 0:
            if intersections[0][1] > intersections[1][1]:
                newvectors = intersections[0]
            else:
                newvectors = intersections[1]

        elif vectors[0] < 0:
            if intersections[0][1] > intersections[1][1]:
                newvectors = intersections[1]
            else:
                newvectors = intersections[0]


        elif vectors[0] == 0 and vectors[1] > 0:
            if intersections[0][0] > intersections[1][0]:
                newvectors = intersections[1]
            else:
                newvectors = intersections[0]

        elif vectors[0] == 0 and vectors[1] < 0:
            if intersections[0][0] > intersections[1][0]:
                newvectors = intersections[0]
            else:
                newvectors = intersections[1]

        elif vectors[1] == 0 and vectors[0] > 0:
            if intersections[0][1] > intersections[1][1]:
                newvectors = intersections[0]
            else:
                newvectors = intersections[1]

        elif vectors[1] == 0 and vectors[0] < 0:
            if intersections[0][1] > intersections[1][1]:
                newvectors = intersections[1]
            else:
                newvectors = intersections[0]


    for i in range(2):
        movement[i] = newvectors[i] - vectors[i]

    return movement

def get_intersections(x0, y0, r0, x1, y1, r1):

    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1
    d = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    # non intersecting
    if d > r0 + r1:
        return None
    # One circle within other
    if d < abs(r0 - r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
        a = (r0 ** 2 - r1 ** 2 + d ** 2) / (2 * d)
        h = math.sqrt(r0 ** 2 - a ** 2)
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d

        x3 = x2 + h * (y1 - y0) / d
        y3 = y2 - h * (x1 - x0) / d
        x4 = x2 - h * (y1 - y0) / d
        y4 = y2 + h * (x1 - x0) / d
        vecs1 = [(x3), (y3)]
        vecs2 = [(x4), (y4)]
        intersections = [vecs1,vecs2]

        return intersections