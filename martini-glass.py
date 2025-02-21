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


widthPrev = int(args[1])
width = widthPrev
if not width % 2:
    width += 1
martini = []

for i in range(width, 0, -2):
    print(makeLine(i, width))
    if i == 2:
        print(makeLine(i-1, width))

for i in range(widthPrev):
    print((widthPrev)*" " + "|")
print("="*width)
