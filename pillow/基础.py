from PIL import Image
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
from PIL import ImageFilter,ImageChops

# 得到图片每一点的灰度并导出表
# print(list_per_pixel)
def GrayValueList():
    Ima=Image.open('灰度图10_10.png')
    Ima.show()
    print(Ima.size)
    print(Ima.format)
    print(Ima.getpixel((1,0))) # 像素点坐标从0开始

    list_per_pixel=[(x,y) for y in range(10) for x in range(10)]
    listOfGrayValue=''
    index=0
    for i in range(100):
        gv=Ima.getpixel(list_per_pixel[i])[0]
        gv=str(gv)
        listOfGrayValue+=gv
        listOfGrayValue+='\t'
        index+=1
        if index==10:
            listOfGrayValue+='\n'
            index=0
    f=open('./灰度表.txt','w')
    f.write(listOfGrayValue)

def blend():
    Ima_yellow=Image.open('./黄色1588_833.png').convert('RGB') # 打开同时转换
    Ima_red=Image.open('./红色1588_833.png').convert('RGB')
    imaBlended=Image.blend(Ima_red,Ima_yellow,alpha=0.3)# 红7黄3
    imaBlended.show()
#blend()

def composit():
    from PIL import Image
    img1=Image.open('.\黄色1588_833.png')
    img2=Image.open('.\GEM.png').convert('RGB')
    img2=img2.resize(img1.size)
    r,g,b=img2.split()# split()方法用于将一个多通道的图像拆分成多个单通道的图像
    Image.composite(img2,img1,g).show() # 绿色越多的地方，im2混合的比例就越大
    g.show() # 一个黑白图，越亮的地方绿色越多
# composit()

def funcForImage(p):
    if p>=125 and p<=230:
        return 220
    elif p>230:
        return 40
    else:
        return 40
def imageFunc():
    img=Image.open('./IMG_20240211_172019.jpg').convert('RGB')
    Image.eval(img,funcForImage).show()
# imageFunc()

tow=Image.open('./2_2.png').convert('RGB')
gem_chill_385_358=Image.open('.\GEM.png').convert('RGB')
sight=Image.open('./IMG_20240211_172019.jpg').convert('RGB')
bigPhoto_gem=Image.open("./1726127735646.jpg").convert('RGB')

def resample_scale():
    img=tow.copy() # 拷贝图片
    # 缩放为指定大小(28,28)
    img.thumbnail((28,28),resample=3)
    """
    Image.NEAREST (0): 最近邻插值，速度快但质量较差。
    Image.BILINEAR (2): 双线性插值，质量较好，速度适中。
    Image.BICUBIC (3): 双三次插值，质量最好，但速度较慢。
    Image.LANCZOS (1): 高质量的滤波器，通常用于需要高质量结果的情况
    """
    img.show()
# resample_scale()

def cutAndPastetoAnotherImg():
    #复制图片
    imgb=tow.copy()
    imgc=gem_chill_385_358.copy()
    #剪切图片
    region=imgb.crop((0,0,300,300)) #从坐标（0,0）到（300,300）的矩形
    #粘贴图片
    imgc.paste(region,(30,30))
    imgc.show()
# cutAndPastetoAnotherImg()

# gem_chill_385_358.rotate(30).show() 图像旋转完还是方形像素，空白处填充黑色

def 合并不同图片的通道():
    from PIL import Image
    img2=sight.resize(gem_chill_385_358.size)
    gem=gem_chill_385_358.copy()
    r1,g1,b1= gem.split()
    r2,g2,b2= img2.split()
    tmp=[r1,g2,b1]
    img = Image.merge("RGB",tmp)
    img.show()
# 合并不同图片的通道()



"""
1. 最小值滤波 (MinFilter)
作用：在每个像素点周围的一个区域内，找到最小值，并将该最小值赋给中心像素。
影响：
较小的滤波器（如 size=3）：可以有效地去除小范围内的亮点噪声（椒盐噪声中的“盐”噪声）。
较大的滤波器（如 size=5 或更大）：可以去除更大范围内的亮点噪声，但可能会过度平滑图像，导致细节丢失。
2. 中值滤波 (MedianFilter)
作用：在每个像素点周围的一个区域内，计算所有像素值的中值，并将该中值赋给中心像素。
影响：
较小的滤波器（如 size=3）：可以有效地去除椒盐噪声，同时保留图像的边缘信息。
较大的滤波器（如 size=5 或更大）：可以去除更大范围内的噪声，但可能会模糊图像的边缘和细节，尤其是在处理纹理丰富的图像时。
3. 模式滤波 (ModeFilter)
作用：在每个像素点周围的一个区域内，找到出现次数最多的像素值（即众数），并将该众数值赋给中心像素。
影响：
较小的滤波器（如 size=3）：可以有效地去除小范围内的噪声，特别适用于处理具有离散值的图像（如二值图像）。

BLUE:模糊
CONTOUR:轮廓
DETAIL:详情
EDGE_ENHANCE：边缘增强
EDGE_ENHANCE_MORE:边缘更多增强
EMBOSS:浮雕
FIND_EDGES:寻找边缘
SHARPEN:锐化
SMOOTH:平滑
"""
noisePhoto=Image.open('./1686927235363.jpg').convert('RGB')
def filter():

    #打开图片
    imga=sight
    w,h=imga.size
    #创建图像区域
    img_output=Image.new('RGB',(2*w,h))
    #将创建的部分粘贴图片
    img_output.paste(imga,(0,0))
    #创建列表存储滤镜
    fltrs=[]
    fltrs.append(ImageFilter.DETAIL)
    # fltrs.append(ImageFilter.MinFilter(size=3))
    # fltrs.append(ImageFilter.ModeFilter(size=5))
    # fltrs.append(ImageFilter.EDGE_ENHANCE)#边缘强化滤镜
    # fltrs.append(ImageFilter.FIND_EDGES) #查找边缘滤镜 不接受参数
    # fltrs.append(ImageFilter.GaussianBlur(10))#高斯模糊滤镜
    for fltr in fltrs:
        r=imga.filter(fltr)
    img_output.paste(r,(w,0))
    img_output.show()
# filter()

def 饱和度等等的色彩调整():
    from PIL import ImageEnhance
    en=ImageEnhance.Color(sight)
    en.enhance(5).show() # 大于一增强，小于1减弱，=1不变
    
# 饱和度等等的色彩调整()








