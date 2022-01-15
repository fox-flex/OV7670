import serial
import time
import pickle
from PIL import Image
import numpy as np

# baud = 2_000_000
# col = 640
# row = 480
baud = 500_000
col = 320
row = 240
# baud = 2_000_000
# col = 160
# row = 120


def run(ser, name):
    new_file_bytes = []
    while len(new_file_bytes) < col*row*2:
        y = ser.inWaiting()
        if y:
            z = ser.read()
            n = len(new_file_bytes)
            if (n % 2000) == 0:
                print(n)
            new_file_bytes.append(z)

    mat = shit(new_file_bytes)
    do_img(mat, name)


def shit(data_array):
    columns = col
    lines = row

    mat = [[[0]*3 for __ in range(columns)] for _ in range(lines)]
    mat = np.array(mat, dtype=np.uint8)
    for ind in range(0, len(data_array), 2):
        x = (ind//2) // columns
        y = (ind//2) % columns
        pixel = (int.from_bytes(data_array[ind], byteorder="big") << 8) |\
                (int.from_bytes(data_array[ind+1], byteorder="big"))
        R = pixel & 0b11111000_00000000
        G = pixel & 0b00000111_11100000
        B = pixel & 0b00000000_00011111
        mat[x, y, 0] = R >> 8
        mat[x, y, 1] = G >> 3
        mat[x, y, 2] = B << 3

    return mat


def do_img(mat, name):
    new_image = Image.fromarray(mat, "RGB")
    new_image.save(name)


# def run2(ser, name):
#     new_file_bytes = []
#     while len(new_file_bytes) < col*row*2:
#         y = ser.inWaiting()
#         if y:
#             z = ser.read()
#             n = len(new_file_bytes)
#             if (n % 2000) == 0:
#                 print(n)
#             new_file_bytes.append(z)
#
#     mat1 = shit(new_file_bytes)
#
#     new_file_bytes = []
#     while len(new_file_bytes) < col * row * 2:
#         y = ser.inWaiting()
#         if y:
#             z = ser.read()
#             n = len(new_file_bytes)
#             if (n % 2000) == 0:
#                 print(n)
#             new_file_bytes.append(z)
#     mat2 = shit(new_file_bytes)
#
#     # mat = (mat1+mat2)/2
#     mat = np.mean(np.array([mat1, mat2]), axis=0)
#     do_img(mat, name)
#


if __name__ == '__main__':
    GPSPort = "/dev/ttyUSB0"
    port = serial.Serial(port=GPSPort, baudrate=baud, bytesize=8, parity='N', stopbits=1, xonxoff=0, rtscts=0)
    print(port)

    run(port, './img/p.jpg')
    for i in range(4):
        run(port, f'./img/p{i}.jpg')
