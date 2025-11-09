from PIL import Image, ImageDraw, ImageFont
imagevar = Image.open("D:\Moonshot\ASCII_SHADER\REDEYES.jpg") #CHECK EXTENSION!!!
imagewidth = imagevar.width
imageheight = imagevar.height

ScaleFactor = 0.2

oneCharWidth = 10 # we have to scale the image based on character width and height to maintain aspect ratio
oneCharHeight = 18 
print(imagewidth,imageheight,imageheight/imagewidth)


# imageload = imagevar.load() #load() method is used to explicitly load the image data into memory when you call image.open it just reads the file header and necessary metadata not the entire image data

imagevar = imagevar.resize((int(imagewidth * ScaleFactor), int(imageheight * ScaleFactor * (oneCharWidth/oneCharHeight) )), Image.NEAREST) #scale the image based on scalefactor

imagewidth = imagevar.width
imageheight = imagevar.height

imageload = imagevar.load() #load() method is used to explicitly load the image data into memory when you call image.open it just reads the file header and necessary metadata not the entire image data
print(imageheight,imagewidth,imageheight/imagewidth)

asciichars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,. " [::-1]
asciilen = len(asciichars)

textfile = open("output.txt", "w") 

fnt = ImageFont.truetype("D:/Moonshot/arial.ttf", 15)
print(fnt)


imagevar = Image.new('RGB', (oneCharWidth * imagewidth, oneCharHeight * imageheight), color=(0,0,0)) #the ascii characters are not square
theight, thewidth = imagevar.size
print(theight,thewidth,theight/thewidth)

Drawimagevar = ImageDraw.Draw(imagevar)

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
        textfile.write(get_asciichar(brightness))

        #drawing action
        Drawimagevar.text((j*oneCharWidth,i*oneCharHeight),get_asciichar(brightness), font=fnt, fill=(r, g, b))
    textfile.write("\n")

imagevar.save("output.jpeg")