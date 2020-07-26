import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

#Myown Function(5)
def upside_down(im):
    n,m = im.dim()
    im2 = Matrix(n,m)
    for i in range(n):
        for j in range(m):
            im2[n-i-1,j] = im[i,j]
    return im2

# Rest of the question

## Code from the lectures of items, local_operator - DO NOT CHANGE ##

def items(mat):
    '''flatten mat elements into a list'''
    n,m = mat.dim()
    lst = [mat[i,j] for i in range(n) for j in range(m)]
    return lst

def local_operator(A, op, k=1):
  n,m = A.dim()
  res = A.copy()  # brand new copy of A
  for i in range(k,n-k):
    for j in range(k,m-k):
      res[i,j] = op(items(A[i-k:i+k+1,j-k:j+k+1]))
  return res

## end of code from lectures


def segment(im, thrd):
    ''' Binary segmentation of image im by threshold thrd '''
    n,m = im.dim()
    im2 = Matrix(n,m)
    for i in range(n):
        for j in range(m):
            if im[i,j] < thrd:
                im2[i,j] = 0
            else:
                im2[i,j] = 255
    return im2

def dilate(im, k=1):
    return local_operator(im, max, k)

#Function edeges (4)
def edges(im, k, thr):
    n,m = im.dim()
    im2 = im.copy()
    im2 = segment(im2, thr)
    dilated_im2 = dilate(im2, k)
    return dilated_im2 - im2

#Function rotate(1)
def rotatePicture(image):
    pixels = list(image.getdata())
    new_pixels = []
    pixel_len = len(pixels)-1
    while (pixel_len>-1):
        new_pixels.append(pixels[pixel_len])
        pixel_len = pixel_len - 1
    print(type(new_pixels))
    return new_pixels

#Function Mirror (2)
def mirrorPicture(image):
    #pixels = list(image.getdata())
    new_image = Image.new("RGB", image.size)
    #width, height = image.size
    a = image.size[0] - 1
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel = image.getpixel((x, y))
            new_image.putpixel((a, y), pixel)
        a -= 1
    return (list(new_image.getdata()))

#Function resize (3)
def resizePicture(image):
    width, height = image.size
    pixel=image.load()
    newpixel = []
    for i in range(height):
        newpixel.append([])
        for j in range(width):
            newpixel[i].append(pixel[j, i])
    newpixel2 = []
    for i in range(0, len(newpixel) - 1, 2):
        newpixel2.append([])
        for j in range(0, len(newpixel[i]) - 1, 2):
            r = (newpixel[i][j][0] + newpixel[i + 1][j][0] + newpixel[i][j + 1][0] + newpixel[i + 1][j + 1][0]) // 4
            g = (newpixel[i][j][1] + newpixel[i + 1][j][1] + newpixel[i][j + 1][1] + newpixel[i + 1][j + 1][1]) // 4
            b = (newpixel[i][j][2] + newpixel[i + 1][j][2] + newpixel[i][j + 1][2] + newpixel[i + 1][j + 1][2]) // 4
            new_value = (r, g, b)
            newpixel2[i // 2].append(new_value)

    return (newpixel2)


