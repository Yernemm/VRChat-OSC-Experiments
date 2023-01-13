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


    t = i / 1000
    r = i / 2000
    #generate x and y from t on a circle with radius r and centre 0.5, 0.5 where x and y are from 0 to 1
    x = math.cos(t * 2 * math.pi) * r + 0.5
    y = math.sin(t * 2 * math.pi) * r + 0.5

    client.send_message("/avatar/parameters/pixel-r", (i / 1000))
    client.send_message("/avatar/parameters/pixel-g", x)
    client.send_message("/avatar/parameters/pixel-b", y)

    client.send_message("/avatar/parameters/pixel-x", x)
    client.send_message("/avatar/parameters/pixel-y", y)
    time.sleep(1/60)

