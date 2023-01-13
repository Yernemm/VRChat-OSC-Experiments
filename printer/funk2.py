import OSCPrinter
import time
from PIL import Image

path = "tT2uu.png"
rate = 10

OSCPrinter.trailOff()
OSCPrinter.particleOff()



#generate a list of all the vertices and edges of a square-based pyramind where x,y,z are in [0,1]
vertices = [
    [0,0,0],
    [1,0,0],
    [1,1,0],
    [0,1,0],
    [0.5,0.5,1]
    ]

edges = [
    [0,1],
    [1,2],
    [2,3],
    [3,0],
    [0,4],
    [1,4],
    [2,4],
    [3,4]
    ]

#generate a list of all the vertices and edges of a cube where x,y,z are in [0,1]
vertices2 = [
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]
]

edges2 = [
    [0,1],
    [0,2],
    [0,4],
    [1,3],
    [1,5],
    [2,3],
    [2,6],
    [3,7],
    [4,5],
    [4,6],
    [5,7],
    [6,7]
]


# generate a path that covers all the edges of the cube
path = []
for edge in edges:
    path.append(vertices[edge[0]])
    path.append(vertices[edge[1]])
    
# print all the edges

OSCPrinter.setup()
OSCPrinter.trailOn()
OSCPrinter.particleOn()

print(len(path));

for point in path:
    OSCPrinter.position(point[0] + 0.0, point[1]+ 0.0, point[2]+ 0.0)
    time.sleep(1/rate)

OSCPrinter.trailOff()