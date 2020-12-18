import random
import angle_generator
import output_manager
import clear_files

vectors = [[0, 0, 0]]
angles = [[0,0,0]]
vectorcount = 10
rotations = 0
angle = 0


clear_files.clearfiles()

for i in range(vectorcount):
    newvectors = [0, 0, 0]
    for j in range(2):
        newvectors[j] = random.randint(-10, 10)
    print(f"new {newvectors}")
    print(f" vec1 {vectors}")
    vectors.append(newvectors)
    print(f" vec2 {vectors}")

for i in range(1, vectorcount+1):
    print(f"\n\nI = {i}")
    print(f"x - {vectors[i][0]}, Y - {vectors[i][1]}")
    xchange = vectors[i][0] - vectors[i-1][0]
    ychange = vectors[i][1] - vectors[i-1][1]
    zchange = vectors[i][2] - vectors[i-1][2]

    z_angle = angle_generator.z_rotation_generator(xchange, ychange)
    angles.append([0, 0, int(z_angle)])


output_manager.print_files(vectors, angles)

print(vectors)
print()
print(angles)