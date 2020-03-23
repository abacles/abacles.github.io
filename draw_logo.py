# ABACLES

from PIL import Image, ImageDraw


def sqdist(pi,pii):
    '''Returns squared distance between two points'''
    return (pi [0] - pii [0])**2 + (pi [1] - pii [1])**2


def dist_in_range(point,focus,dist):
    '''Returns whether point is less than dist units away from focus'''
    return sqdist(point,focus) < dist**2


def leftstroke(x):
    '''Returns corresponding y given x for the linear function that draws the left side of A'''
    # Bottom left start: (padding,size-padding)
    if x < padding or x > size/2:
        return None
    return (size-padding) - (x-padding)*2

def rightstroke(x):
    '''Returns corresponding y given x for the linear function that draws the right side of A'''
    # Bottom right start: (size-padding,size-padding)
    if x-thickness//2 <= size/2 or x > size-padding:
        return None
    return (size-padding) - ((size-padding)-x)*2


def draw_abacles(x,y):
    '''Draw an abacles centered at x,y'''
    focus = (x+abacleslen//2+abacleswid//2,y)
    grate = 1.0*gradient / (abacleslen+abacleswid)
    for i in range(x-abacleslen//2,x+abacleslen//2):
        d = int(grate*(focus [0]-i))
        for j in range(y-abacleswid//2,y+abacleswid//2):
            pixboard [j*size + i] = (color [0]+d,color [1]+d,color [2]+d)
    for i in range(x-abacleslen//2-abacleswid//2,x-abacleslen//2):
        d = int(grate*(focus [0]-i))
        for j in range(y-abacleswid//2,y+abacleswid//2):
            if dist_in_range((i,j),(x-abacleslen//2,y),abacleswid//2):
                pixboard [j*size + i] = (color [0]+d,color [1]+d,color [2]+d)
    for i in range(x+abacleslen//2,x+abacleslen//2+abacleswid//2):
        d = int(grate*(focus [0]-i))
        for j in range(y-abacleswid//2,y+abacleswid//2):
            if dist_in_range((i,j),(x+abacleslen//2,y),abacleswid//2):
                pixboard [j*size + i] = (color [0]+d,color [1]+d,color [2]+d)


size = int(input('Size: '))

padding = size//8
thickness = size//10
abacleslen = size//4
abacleswid = abacleslen//2


color = (40,100,200)
gray = (255,255,255)
gradient = 100
ggradlen = size - 2*padding
ggrad = tuple(1.0*(gray [i]-color [i])/ggradlen for i in range(3))

im = Image.new('RGB',(size,size))
pixboard = [(255,255,255)]*size**2


for xc in range(padding,size-padding+1):
    for yc in range(padding,size-padding+1):
        ydraw = leftstroke(xc)
        if ydraw != None and 0 <= yc-ydraw <= 1:
            pixboard [yc*size + xc : yc*size + xc + thickness + 1] = [color] * (thickness+1)
        ydraw = rightstroke(xc)
        if ydraw != None and 0 <= yc-ydraw <= 1:
            for i in range(thickness+1):
                if pixboard [yc*size + xc - i] != color:
                    pixboard [yc*size + xc - i] = tuple(int(gray [i] - ggrad [i]*(yc-padding-thickness)) for i in range(3)) # padding+thickness is slightly above the intersection of the left and right stroke

draw_abacles(int(padding + (size-2*padding)*0.3),int(padding + (size-2*padding)*0.6))


im.putdata(pixboard)


fname = input('Save in: ')
im.save(fname + '.png')
im.show()
