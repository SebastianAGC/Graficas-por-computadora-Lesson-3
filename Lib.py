
def getPossibleValues(pixels):
    array = []
    step = 2 / pixels
    start = -1
    while start < 1:
        array.append(start)
        start = start + step
    return array

def normalize(x, y, viewPort):
    newX = int((x + 1) * (viewPort["width"] / 2) + viewPort["x"])
    newY = int((y + 1) * (viewPort["heigth"] / 2) + viewPort["y"])
    return newX, newY