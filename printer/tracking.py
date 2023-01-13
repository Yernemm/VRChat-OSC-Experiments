import random
import time

from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 9000)

_noise = 0.4
_rate = 30

def noise():
    return random.uniform(-_noise, _noise)

trackers = [
    [-.4, -0.2, 0.0],
    [0.4, -0.2, 0.0],
    [0.1, -1.8, 0.0],
    [-0.1, -1.8, 0.0],
    [0.0, -0.7, 0.0]
]

while True:

    client.send_message("/tracking/trackers/head/position", [0.0, 0.0, 0.0])
    client.send_message("/tracking/trackers/head/rotation", [0.0, 0.0, 0.0])

    for ii in range(len(trackers)):
        #6 random offsets -0.1 to 0.1

        i = ii + 1

        client.send_message(f"/tracking/trackers/{i}/position", 
        [trackers[ii][0] + noise(), 
        trackers[ii][1] + noise(), 
        trackers[ii][2] + noise()])
        client.send_message(f"/tracking/trackers/{i}/rotation", [0.0  + noise(), 0.0 +  + noise(), 0.0 + noise()])
    time.sleep(1 / _rate)

