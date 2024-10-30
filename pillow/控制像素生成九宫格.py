from PIL import Image, ImageFilter, ImageFont, ImageDraw
width=300;height=300
x,y=0,0
im = Image.new("RGB",(width,height),(255,255,255)) #最后一个参数是背景颜色，像素
draw = ImageDraw.Draw(im)
def get_color1():
    a = (x//100)+(y//100)
    if a == 0:
        return (255,0,0)
    elif a == 1:
        return (0,255,255)
    elif a ==2:
        return (0,0,255)
    elif a==3:
        return (255,255,0)
    elif a==4:
        return (255,0,255)
    else:
        return (0,0,0)
    #填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=get_color1())
im.show()