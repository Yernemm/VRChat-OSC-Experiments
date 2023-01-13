import OSCPrinter
import time
from PIL import Image

path = "amogus.jpg"
rate = 60

print("Loading image...")
im = Image.open(path)
print("Reformatting image...")
im = im.resize((64, 64), Image.LANCZOS)
im = im.convert("RGB")
print("Sending pixels...")
OSCPrinter.trailOff()
OSCPrinter.particleOff()
OSCPrinter.setup()
OSCPrinter.particleOn()
#OSCPrinter.trailOn()
for y in range(0,64):
    for x in range(0,64):
        r, g, b = im.getpixel((x, y))
        OSCPrinter.color255(r, g, b)
        OSCPrinter.position(r/255, g/255, b/255)
        time.sleep(1/rate)
    print(f"Row {y + 1} sent.")