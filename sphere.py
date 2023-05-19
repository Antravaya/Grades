import math

def sphereArea(radius):
    return 4 * math.pi * math.pow(radius, 2)


def sphereVolume(radius):
    return (4/3) * math.pi * math.pow(radius, 3)


def main():
    radius = eval(input("Enter a radius of sphere: "))
    area = sphereArea(radius)
    vol = sphereVolume(radius)

    print("Area is {0:0.2f}".format(area))
    print("Volume is {0:0.2f}".format(vol))

main()
