from PIL import Image
imagevar = Image.open("D:\Moonshot\ASCII_SHADER\sololevel.jpeg")
imagewidth = imagevar.width
imageheight = imagevar.height

imageload = imagevar.load() #load() method is used to explicitly load the image data into memory when you call image.open it just reads the file header and necessary metadata not the entire image data

asciichars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,. "
asciilen = len(asciichars)


print(imageheight)
print(imagewidth)

def get_asciichar(brightness):
    #I need to map 0-255 brightness to 0-asciilen
    unit = 256 / asciilen
    ascii_index = int(brightness / unit)
    return asciichars[ascii_index]

for i in range(imageheight):
    for j in range(imagewidth):
        r, g, b = imageload[j,i] #imageload[j, i] accesses the pixel at column j, row i (note: it's [x, y] format), This returns a tuple like (255, 128, 0) containing three values
        brightness = int(r/3 + g/3 + b/3) #take rgb average for brigtness value
        imageload[j,i] = (brightness, brightness, brightness)

imagevar.save("output.jpeg")