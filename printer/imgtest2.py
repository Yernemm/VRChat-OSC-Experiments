import random
import time
import math

from pythonosc import udp_client
from PIL import Image

print("Loading image...")

im = Image.open("jermasussy.jpg")

print("Reformatting image...")
im = im.resize((64, 64), Image.LANCZOS)
im = im.convert("RGB")

print("Connecting to OSC...")
client = udp_client.SimpleUDPClient("127.0.0.1", 9000)


print("Starting print...")
#print-start
client.send_message("/avatar/parameters/print-start", False)
time.sleep(0.1)
client.send_message("/avatar/parameters/print-start", True)
time.sleep(0.05)


print("Sending pixels...")
for y in range(0,64):
    for x in range(0,64):
        r, g, b = im.getpixel((x, y))

        client.send_message("/avatar/parameters/pixel-r", r / 255)
        client.send_message("/avatar/parameters/pixel-g", g / 255)
        client.send_message("/avatar/parameters/pixel-b", b / 255)

        #client.send_message("/avatar/parameters/pixel-r", random.uniform(0, 1))
        #client.send_message("/avatar/parameters/pixel-g", random.uniform(0, 1))
        #client.send_message("/avatar/parameters/pixel-b", random.uniform(0, 1))

        client.send_message("/avatar/parameters/pixel-x", x / 64)
        client.send_message("/avatar/parameters/pixel-y", y / 64)
        client.send_message("/avatar/parameters/pixel-z", r / 255)
        #client.send_message("/avatar/parameters/pixel-x", random.uniform(0, 1))
        #client.send_message("/avatar/parameters/pixel-y", random.uniform(0, 1))
        time.sleep(1/60)
        
    print(f"Row {y + 1} sent.")