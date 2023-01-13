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


for i in range(500):
    client.send_message("/avatar/parameters/pixel-r", 0.8* (i / 500))
    client.send_message("/avatar/parameters/pixel-g", 0.1)
    client.send_message("/avatar/parameters/pixel-b", 0.1)

    t = i / 500
    #generate x and y from t on a circle where x and y are from 0 to 1
    x = math.cos(t * 2 * math.pi) / 2 + 0.5
    y = math.sin(t * 2 * math.pi) / 2 + 0.5
   

    client.send_message("/avatar/parameters/pixel-x", x)
    client.send_message("/avatar/parameters/pixel-y", y)
    time.sleep(1/60)


for i in range(500):
    client.send_message("/avatar/parameters/pixel-r", 0.2)
    client.send_message("/avatar/parameters/pixel-g", 0.05)
    client.send_message("/avatar/parameters/pixel-b", 0.9 * (i / 500))

    t = i / 500
    #generate x and y from t on a circle where x and y are from 0.25 to 0.75
    x = math.cos(t * 2 * math.pi) / 2 + 0.5
    y = math.sin(t * 2 * math.pi) / 2 + 0.5
    x = x * 0.5 + 0.25
    y = y * 0.5 + 0.25
   

    client.send_message("/avatar/parameters/pixel-x", x)
    client.send_message("/avatar/parameters/pixel-y", y)
    time.sleep(1/60)