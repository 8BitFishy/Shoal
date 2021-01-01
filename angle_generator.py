import math

def angle_generator(duration, actorlist):
    for i in range(1, duration + 1):
        print(f"Frame - {i} of {duration}")
        for Actor in actorlist:

            rotationchanges = generate_angles(Actor.vectors, Actor.angles, i)

            Actor.angles.append([rotationchanges[0], 0, Actor.angles[i - 1][2] + rotationchanges[2]])

    return actorlist

def generate_angles(vectors, angles, i):
    xchange = vectors[i][0] - vectors[i - 1][0]
    ychange = vectors[i][1] - vectors[i - 1][1]
    zchange = vectors[i][2] - vectors[i - 1][2]
    rotationchanges = [0, 0, 0]
    #generate z angle
    current_angle = angles[i - 1][2]
    zrotationchange = generate_rotationchange(current_angle, xchange, ychange, i, angles)
    rotationchanges[2] = zrotationchange

    #generate x angle
    xrotationchange = generate_xrotationchange(zchange, math.sqrt(((abs(xchange))**2) + ((abs(ychange))**2)))
    rotationchanges[0] = xrotationchange

    return rotationchanges


def generate_rotationchange(current_angle, xchange, ychange, i, angles):
    # Calculate necessary angle for movement
    z_angle = target_angle_generator(xchange, ychange, i, angles)
    # simplify current angle to 0-360deg range
    current_angle_simplified = (current_angle % 360)
    rotationchange = z_angle - current_angle_simplified

    if rotationchange >= 180:
        rotationchange = current_angle_simplified + (360 - z_angle)
        rotationchange = -rotationchange

    elif rotationchange < -180:
        rotationchange = z_angle + (360 - current_angle_simplified)

    return rotationchange


def target_angle_generator(xchange, ychange, i, angles):
    if xchange > 0 and ychange > 0:
        #if both are moving positive
        if xchange > ychange:
            angle = (90+ abs((45 * (ychange / xchange))))

        else:
            angle = (180 - abs((45 * (xchange / ychange))))

    elif xchange < 0 and ychange < 0:

        if abs(xchange) > abs(ychange):
            angle = (270 + abs((45 * (ychange / xchange))))

        else:
            angle = (360 - abs((45 * (xchange / ychange))))

    elif xchange > 0 and ychange < 0:
        if abs(xchange) > abs(ychange):
            angle = (90 - abs((45 * (ychange / xchange))))

        else:
            angle = (abs((45 * (xchange / ychange))))

    elif ychange > 0 and xchange < 0:
        if abs(xchange) > abs(ychange):
            angle = (270 - abs((45 * (ychange / xchange))))

        else:
            angle = (180 + abs((45 * (xchange / ychange))))

    elif xchange == 0 and ychange != 0:
        if ychange > 0:
            angle = 180
        else:
            angle = 0

    elif ychange == 0 and xchange != 0:
        if xchange > 0:
            angle = 90
        else:
            angle = 270

    else:
        angle = angles[i-1][2]%360
    return(angle)


def generate_xrotationchange(zchange, hypo):
    angle = math.atan(zchange/hypo)
    angle = angle * (180 / math.pi)
    angle = -angle

    return angle