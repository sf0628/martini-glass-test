import sys
import math
args = sys.argv

if len(args) != 2 and args[1].isnumeric():
    print("Invalid input. Please input one number greater than 0!")
    quit()


def makeLine(glass, width):
    space = math.floor(width - glass / 2)
    line = ""
    # initial space
    line += " "*space
    # middle percentage signs
    line += "%"*glass
    return line


width = int(args[1])
widthAdj = width
if not width % 2:
    widthAdj += 1
martini = []

for i in range(width, 0, -2):
    print(makeLine(i, width))
    if i == 2:
        print(makeLine(i-1, width))

for i in range(width):
    print((width-1)*" " + "|")
print("  " + "="*width)
