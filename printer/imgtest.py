import random
import time

from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 9000)

while True:
    client.send_message("/avatar/parameters/pixel-r", random.uniform(0, 1))
    client.send_message("/avatar/parameters/pixel-g", random.uniform(0, 1))
    client.send_message("/avatar/parameters/pixel-b", random.uniform(0, 1))
    time.sleep(0.1)