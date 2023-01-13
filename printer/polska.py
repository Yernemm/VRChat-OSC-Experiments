import random
import time

from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 9000)

client.send_message("/avatar/parameters/Lock", False)
client.send_message("/avatar/parameters/off", False)
client.send_message("/avatar/parameters/Zytnowka", True)
client.send_message("/avatar/parameters/kask", True)
client.send_message("/avatar/parameters/Drink", False)
client.send_message("/avatar/parameters/Emote", 0)

#client.send_message("/avatar/parameters/Emote", 0)

#for i in range(9999):
    #client.send_message("/avatar/parameters/Emote", i)
    #print(i)
    #time.sleep(0.01)