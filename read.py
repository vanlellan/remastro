
from PIL import Image
import io
import sys

# TODO
#   Read bytes in chunks rather than 1 by 1
#       will need to write flush bytes to fifo.mjpg after gphoto2 command finishes

numImages = int(sys.argv[1])

with open("fifo.mjpg","rb") as f:
    for i in range(numImages):
        byte = f.read(1)
        goodData = False
        while True:
            oldbyte = byte
            byte = f.read(1)
            if oldbyte == b'\xff' and byte==b'\xd8':
                goodData = True
                data = oldbyte
            if oldbyte == b'\xff' and byte==b'\xd9':
                goodData = False
                data = data+byte
                i += 1
                break
            if goodData:
                data = data+byte
        im = Image.open(io.BytesIO(data))
        im.save("image"+str(i)+".png")


