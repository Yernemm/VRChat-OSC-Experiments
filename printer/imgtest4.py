import random
import time
import math

from pythonosc import udp_client


print("Loading image...")



print("Reformatting image...")


print("Connecting to OSC...")
client = udp_client.SimpleUDPClient("127.0.0.1", 9000)


print("Starting print...")
#print-start
client.send_message("/avatar/parameters/print-start", False)
time.sleep(0.1)
client.send_message("/avatar/parameters/print-start", True)
time.sleep(0.05)


for i in range(1000):
    #draw a sine wave
    client.send_message("/avatar/parameters/pixel-r", 0.8* (i / 1000))
    client.send_message("/avatar/parameters/pixel-g", 0.1)
    client.send_message("/avatar/parameters/pixel-b", 0.1)

    t = i / 1000
    t = t * 4
    #generate x and y on a sine wave where x and y are from 0 to 1
    x = i / 1000

    y = math.sin(t * 2 * math.pi) / 2 + 0.5
    #y = math.tanh(t)
    #y = y / 2 + 0.5
    y = y

    client.send_message("/avatar/parameters/pixel-x", x)
    client.send_message("/avatar/parameters/pixel-y", y)
    time.sleep(1/60)