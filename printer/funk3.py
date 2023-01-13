import OSCPrinter
import time
import random
from PIL import Image

path = "tT2uu.png"
rate = 10

OSCPrinter.trailOff()
OSCPrinter.particleOff()

#generate a list of all the vertices and edges of a square-based pyramind where x,y,z are in [0,1]
# print all the edges

OSCPrinter.setup()
OSCPrinter.trailOn()
OSCPrinter.particleOn()

while(True):
    OSCPrinter.position(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))
    OSCPrinter.color255(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    time.sleep(1/rate)



OSCPrinter.trailOff()