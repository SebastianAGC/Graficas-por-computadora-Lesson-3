# Sebastián Galindo 15452
# Gráficas por computadora
# Código obtenido de http://www.roguebasin.com/index.php?title=Bresenham%27s_Line_Algorithm

from Bitmap import *
from Lib import *

screen = None
viewPort = {"x": 0, "y": 0, "width": 0, "heigth": 0}
blue = color(0, 0, 255)
red = color(255, 0, 0)
green = color(0, 255, 0)
colorStandard = 255

sign = lambda a: (a > 0) - (a < 0)


def glInit():
    pass


def glCreateWindow(width, heigth):
    global screen
    screen = Bitmap(width, heigth)


def glViewPort(x, y, width, heigth):
    global viewPort
    viewPort["x"] = x
    viewPort["y"] = y
    viewPort["width"] = width
    viewPort["heigth"] = heigth


def glClear():
    screen.clear()


def glClearColor(r, g, b):
    screen.color = color(r, g, b)


# Recibe parametros entre -1 y 1
def glVertex(x, y):
    global viewPort
    global screen
    newX = int((x + 1) * (viewPort["width"] / 2) + viewPort["x"])
    newY = int((y + 1) * (viewPort["heigth"] / 2) + viewPort["y"])
    screen.point(newX, newY, screen.currentColor)


def glColor(r, g, b):
    r = int(r * colorStandard)
    g = int(g * colorStandard)
    b = int(b * colorStandard)
    screen.currentColor = color(r, g, b)


def glLine(x0, y0, x1, y1):
    global viewPort
    global screen
    x0, y0 = normalize(x0, y0, viewPort)
    x1, y1 = normalize(x1, y1, viewPort)

    # Setup initial conditions
    dx = x1 - x0
    dy = y1 - y0

    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)

    # Rotate line
    if is_steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    # Swap start and end points if necessary and store swap state
    swapped = False
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
        swapped = True

    # Recalculate differentials
    dx = x1 - x0
    dy = y1 - y0

    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y0 < y1 else -1

    # Iterate over bounding box generating points between start and end
    y = y0
    points = []
    for x in range(x0, x1 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()

    for point in points:
        screen.point(point[0], point[1], screen.currentColor)


def glFinish():
    screen.write('out.bmp')


def glLoad(name):
    global screen
    model = Obj(name)
    for face in model.vfaces:
        vcount = len(face)
        for j in range(vcount):
            f1 = face[j][0]
            f2 = face[(j + 1) % vcount][0]

            v1 = model.vertices[f1 - 1]
            v2 = model.vertices[f2 - 1]

            x1, y1 = v1[0], v1[1]
            x2, y2 = v2[0], v2[1]
            glLine(x1, y1, x2, y2)
