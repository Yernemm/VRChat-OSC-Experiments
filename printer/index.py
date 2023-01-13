"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import random
import time

from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 9000)

p1 = "/avatar/parameters/LeggingChange"
r1 = 5
p2 = "/avatar/parameters/ShirtChange"
r2 = 11
p3 = "/avatar/parameters/SkinChange"
r3 = 11

rc1 = 0
rc2 = 0
rc3 = 0

toggles = [
    "/avatar/parameters/Horns", 
    "/avatar/parameters/Thurun(Knife)",
    "/avatar/parameters/MagicHat",
    "/avatar/parameters/CyberGasMask",
    "/avatar/parameters/Wings",
    "/avatar/parameters/Ears",
    "/avatar/parameters/FloofyTail",
    "/avatar/parameters/FloofyTails(8Tails)",
    "/avatar/parameters/HoloMask"]


while True:
    new1 = random.randint(0, r1)
    new2 = random.randint(0, r2)
    new3 = random.randint(0, r3)
    client.send_message(p1, new1)
    client.send_message(p2, new2)
    client.send_message(p3, new3)

    for toggle in toggles:
        client.send_message(toggle, random.randint(0, 1))

    client.send_message("/chatbox/input", [f"Options: {new1} {new2} {new3}", True])

    time.sleep(0.5)


# client.send_message("/input/Vertical", 1.0)
# time.sleep(1)
# client.send_message("/input/Vertical", -1.0)
# time.sleep(1)
# client.send_message("/input/Vertical", 0.0)

# for x in range(10):
#     #client.send_message("/filter", random.random())
#     #time.sleep(1)
#     client.send_message("/input/Jump", True)
#     time.sleep(.2)
#     client.send_message("/input/Jump", False)
#     time.sleep(.8)