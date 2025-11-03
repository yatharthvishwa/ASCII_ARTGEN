from PIL import Image
imagevar = Image.open("D:\Moonshot\ASCII_SHADER\sololevel.jpeg")
imagewidth = imagevar.width
imageheight = imagevar.height

imageload = imagevar.load() #load() method is used to explicitly load the image data into memory when you call image.open it just reads the file header and necessary metadata not the entire image data

print(imageheight)
print(imagewidth)

for i in range(imageheight):
    for j in range(imagewidth):
        r, g, b = imageload[j,i] #imageload[j, i] accesses the pixel at column j, row i (note: it's [x, y] format), This returns a tuple like (255, 128, 0) containing three values
        h = int(r/3 + g/3 + b/3) #take rgb average
        imageload[j,i] = (h, h, h) 

imagevar.save("output.jpeg")