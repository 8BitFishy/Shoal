
def z_rotation_generator(xchange, ychange):


    #print(f"Stage {i}")
    print(f"xchange = {xchange}")
    print(f"ychange = {ychange}")
    #print(f"zchange = {zchange}")

    rotations = 0

    #print(f"Rotations = {rotations}")

    if xchange > 0 and ychange > 0:
        if xchange > ychange:

            print(f"Both positive 1 - {(ychange / xchange)}")
            print(f"Angle = {(90+abs((45 * (ychange / xchange))))+rotations}")
            angle = (90+ abs((45 * (ychange / xchange))))+rotations

        else:

            print(f"Both positive 2 - {(xchange / ychange)}")
            print(f"Angle = {(180 - abs((45 * (xchange / ychange)))+rotations)}")
            angle = (180 - abs((45 * (xchange / ychange)))+rotations)

    elif xchange < 0 and ychange < 0:

        if abs(xchange) > abs(ychange):
            print(f"Both negative 1 - {(ychange / xchange)}")
            print(f"Angle = {(270+abs((45 * (ychange / xchange))))+rotations}")
            angle = (270+ abs((45 * (ychange / xchange))))+rotations

        else:
            print(f"Both negative 2 - {(xchange / ychange)}")
            print(f"Angle = {(360 - abs((45 * (xchange / ychange)))+rotations)}")
            angle = (360 - abs((45 * (xchange / ychange)))+rotations)

    elif xchange > 0 and ychange < 0:
        if abs(xchange) > abs(ychange):
            print(f"X Positive, Y negative, x larger - {ychange / xchange}")
            print(f"Angle = {(90 - abs((45 * (ychange / xchange)))+rotations)}")
            angle = (90 - abs((45 * (ychange / xchange)))+rotations)

        else:
            print(f"X Positive, Y negative, y larger - {xchange / ychange}")
            print(f"Angle = {(abs((45 * (xchange / ychange)))+rotations)}")
            angle = (abs((45 * (xchange / ychange)))+rotations)

    elif ychange > 0 and xchange < 0:
        if abs(xchange) > abs(ychange):
            print(f"Y Positive, X negative, x larger - {ychange / xchange}")
            print(f"Angle = {(270 - abs((45 * (ychange / xchange)))+rotations)}")
            angle = (270 - abs((45 * (ychange / xchange)))+rotations)

        else:
            print(f"Y Positive, X negative, y larger - {xchange / ychange}")
            print(f"Angle = {(180 + abs((45 * (xchange / ychange))) + rotations)}")
            angle = (180 + abs((45 * (xchange / ychange))) + rotations)

    elif xchange == 0 and ychange != 0:
        print(f"xchange zero - {1}")
        if ychange > 0:
            print(f"Angle = 180")
            angle = rotations + 180
        else:
            print(f"Angle = 0")
            angle = rotations + 0


    elif ychange == 0 and xchange != 0:
        print(f"ychange zero - {1}")
        if xchange > 0:
            print(f"Angle = 90")
            angle = rotations + 90
        else:
            print(f"Angle = 270")
            angle = rotations + 270

    else:
        print(f"Both zero - {0}")
        #print(f"i = {i}")
        angle = angles[i-1][2]

    print(f"Angle = {angle}")
    return(angle)
    #rotations = angles[i][2]//360
    #rotations = rotations * 360