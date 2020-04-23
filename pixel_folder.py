from PIL import Image
import os

image = []
# read the image from folder
for f in os.listdir('.'):
    if f.endswith('png'):
        image.append(f)

for i in image:
    img = Image.open(i)
    pixels = img.load()
    for i in range(img.size[0]):  # for every pixel:
        for j in range(img.size[1]):
            if pixels[i, j] != (0, 0, 0):
                # change to black if not red
                pixels[i, j] = (255, 255, 255)
                name = '/Users/tracy/Desktop/Image_Processing/test/new'
                img.save(name,'png')
                #fn, fext = os.path.splitext()
                # i.thumbnail(size_128)
                #img.save('/Users/tracy/Desktop/Image_Processing/test/new')
    #img.show()
    # img.show()
#这一个可以用来改变图像像素以及展示
    # pixels = img.load()
    # for i in range(img.size[0]):
    # for j in range(img.size[1]):
    # if pixels[i, j] != (0, 0, 0):
    # pixels[i, j] = (255, 255, 255)
    # img.save('new/{}{}'.bmp)
# img.show()
