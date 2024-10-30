from PIL import Image, ImageFilter, ImageFont, ImageDraw
import random
width=100
height=100
#最后一个参数是背景颜色，像素默认值
im = Image.new("RGB",(width,height),(255,255,255)) #最后一个参数是背景颜色，像素
draw = ImageDraw.Draw(im)
#获取颜色
def get_color1():
   return (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))
# 获取一个字母或数字
def get_char():
   return chr(random.randint(65,90)) # 在ASCII编码中，65至90的整数对应的是大写英文字母A到Z
#填充每个像素

for x in range(width):
   for y in range(height):
      draw.point((x,y),fill=get_color1())
font = ImageFont.truetype('simsun.ttc', 36)
for i in range(4):
   draw.text((10+i*20,50),get_char(),font=font,fill=(255,0,0))
#干扰线
for i in range(2):
   draw.line(((10,10),(80,80)),fill=(0,255,0),width=3)
im.show()


"""
这段代码的主要目的是生成一个包含随机字符的图像，并添加一些视觉上的干扰（如随机颜色的像素和线条），通常这种图像被称为验证码图像。下面是代码的具体解释：

1. **导入模块**：
   - `from PIL import Image, ImageFilter, ImageFont, ImageDraw` 导入了PIL库中用于图像处理的几个类。
   - `import random` 导入了Python的标准库random，用于生成随机数。

2. **设置图像尺寸**：
   - `width=100` 和 `height=100` 定义了生成图像的宽度和高度。

3. **创建新图像**：
   - `im = Image.new("RGB",(width,height),(255,255,255))` 创建了一个新的RGB模式的图像，尺寸为100x100像素，背景色为白色（255,255,255）。

4. **创建绘图对象**：
   - `draw = ImageDraw.Draw(im)` 创建了一个绘图对象，允许在图像上绘制图形和文本。

5. **定义颜色和字符生成函数**：
   - `get_color1()` 函数生成一个随机的浅色系颜色。
   - `get_char()` 函数生成一个大写字母A-Z之间的随机字符。

6. **填充图像的每个像素**：
   - `for x in range(width): for y in range(height): draw.point((x,y),fill=get_color1())` 这段代码遍历图像的每一个像素位置，并使用随机颜色填充每个像素点，这会在背景上形成一种随机颜色噪点的效果。

7. **在图像上绘制随机字符**：
   - `font = ImageFont.truetype('simsun.ttc', 36)` 加载了一个字体文件（这里使用的是宋体，字号为36），用于后续的文本绘制。
   - `for i in range(4): draw.text((10+i*20,50),get_char(),font=font,fill=(255,0,0))` 在图像上随机位置绘制4个红色的大写字母。每个字符的位置通过计算得出，确保它们不会重叠。

8. **添加干扰线**：
   - `for i in range(2): draw.line(((10,10),(80,80)),fill=(0,255,0),width=3)` 绘制两条绿色的直线作为干扰线，这些线可以帮助防止简单的图像识别软件轻易地读取图像中的字符。

9. **显示图像**：
   - `im.show()` 将生成的图像显示出来。

这样的图像常用于网站登录或表单提交等场景，用来验证用户是否为真实的人类，而不是自动化的程序或机器人。通过要求用户识别并输入图像中的字符，可以有效阻止自动化攻击。
"""