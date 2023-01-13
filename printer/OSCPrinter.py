## OSC Printer ##
# by Yernemm 


from pythonosc import udp_client
import time
from PIL import Image

client = udp_client.SimpleUDPClient("127.0.0.1", 9000)

rate = 60

# Define the function called 'color' that takes three arguments called 'r', 'g', and 'b'
def color(r: float, g: float, b: float):
    # Send the value of 'r' to the avatar parameter named 'pixel-r'
    client.send_message("/avatar/parameters/pixel-r", r)
    # Send the value of 'g' to the avatar parameter named 'pixel-g'
    client.send_message("/avatar/parameters/pixel-g", g)
    # Send the value of 'b' to the avatar parameter named 'pixel-b'
    client.send_message("/avatar/parameters/pixel-b", b)

def color255(r, g, b):
    color(r/255, g/255, b/255)

def position(x: float, y: float, z: float):
    # move avatar to (x, y, z)
    client.send_message("/avatar/parameters/pixel-x", x)
    client.send_message("/avatar/parameters/pixel-y", y)
    client.send_message("/avatar/parameters/pixel-z", z)

def setup():
    print("Starting print...")
    client.send_message("/avatar/parameters/print-start", False)
    time.sleep(0.1)
    client.send_message("/avatar/parameters/print-start", True)
    time.sleep(0.05)

def printImage(path):
    print("Loading image...")
    im = Image.open(path)
    print("Reformatting image...")
    im = im.resize((64, 64), Image.LANCZOS)
    im = im.convert("RGB")
    print("Sending pixels...")
    trailOff()
    particleOff()
    setup()
    particleOn()
    for y in range(0,64):
        for x in range(0,64):
            r, g, b = im.getpixel((x, y))
            color255(r, g, b)
            position(x/64, y/64, 0.0)
            time.sleep(1/rate)
        print(f"Row {y + 1} sent.")

def particleOn():
    client.send_message("/avatar/parameters/particle-emit", True)

def particleOff():
    client.send_message("/avatar/parameters/particle-emit", False)

def trailOn():
    client.send_message("/avatar/parameters/trail-emit", True)

def trailOff():
    client.send_message("/avatar/parameters/trail-emit", False)