from PIL import Image, ImageFilter, ImageFont, ImageDraw
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
im = Image.open("./GEM.png")
draw = ImageDraw.Draw(im)
def get_color(oldColor):
    ''' 如果是黄色(255,255,0)，则换算成红色,把绿色通道置为 0
    可以点击：windows 中的画图软件调色板观察黄色的区间。
    :return:
    '''
    #print(oldColor)
    num=30
    if oldColor[2]-oldColor[1]>num and oldColor[2]-oldColor[0]>num:
        return (oldColor[0]*2,oldColor[1]//4,oldColor[2]//4)
    else:
        return oldColor
for x in range(im.width):
    for y in range(im.height):
        draw.point((x,y),fill=get_color(im.getpixel((x,y))))
im.show()
"""
假设我们有一个图像对象 img，并且想要将位于 (100, 150) 的像素的颜色设置为红色，可以这样写：

python
深色版本
img.putpixel((100, 150), (255, 0, 0))
"""