import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
from time import sleep
from PIL import Image
def main():
    size = os.get_terminal_size()
    size = (size.lines, size.columns)
    # size = (100, 100)
    video_loop(size)

def video_loop(size):
    camera = cv2.VideoCapture(0)
    try:
        while True:
            ret, frame = camera.read()
            brightness = process_frame(frame, size)
            print_image(brightness)
    finally:
        camera.release()
    
def process_frame(frame, windowSize):
    image = np.array(Image.fromarray(frame).convert('L'))
    brightness = np.empty(shape=windowSize, dtype=str)
    x, y = image.shape
    xScale = int(np.floor(x / windowSize[0]))
    yScale =  int(np.floor(y / windowSize[1]))
    
    for i in range(windowSize[0]):
        for j in range(windowSize[1]):
            brightness[i, j] = get_brightness(image[i * xScale, j * yScale])
    return brightness

def get_brightness(val):
    # lightlevels = "%%#########********+++++++++========---------:::::      "[::-1]
    # lightlevels = """Oo. """[::-1]
    # lightlevels = """       .:-i|=+%O#@"""
    lightlevels = """Ñ@#W$9876543210?!abc;:+=-,._                    """[::-1]
    return lightlevels[int((val / 255.0) * (len(lightlevels) - 1))]

def print_image(image):
    stri = ""
    for x in range(0, image.shape[0]):
        for y in range(image.shape[1]):
            stri += image[x, y]
        stri += "\n"
    os.system('cls' if os.name == 'nt' else 'clear')
    print(stri)


if __name__ == "__main__":
    main()