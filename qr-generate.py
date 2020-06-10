#!/usr/bin/env python3

import qrcode, pathlib

data = input("Enter URL: ")

filename = input("Enter filename: ")
filename = filename + ".png"

img = qrcode.make(data)
img.save(filename)

print("File saved to: " + str(pathlib.Path(__file__).parent.absolute()) + "/" + filename)
