from PIL import Image
import numpy as np
import os
import pickle
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
image_path = './GEM.png'  # 原始图片的路径
result_path = './Binoutput.png'  # 处理后图片的保存路径
array_file = './arr.bin'  # 存放一维数组的文件

# 将单个图片转换为一维数组并保存

def image_to_array(image_path, array_file):
    img = Image.open(image_path).convert('RGB')
    # 将图片按三色提取
    r, g, b = img.split() # 每个通道的图像对象都是一个二维数组
    # 将 R、G、B 分别转换为一维数组
    r_arr = np.array(r).reshape(-1) # np.array(r) 这一部分将 r 转换为一个 NumPy 数组。 reshape(-1):这一部分将二维数组展平为一维数组
    g_arr = np.array(g).reshape(-1)
    b_arr = np.array(b).reshape(-1)
    # 将三色数组拼接在一起
    image_arr = np.concatenate((r_arr, g_arr, b_arr)) #形成一个新的更大的一维数组 image_arr

    # 将大的一维数组保存到文件
    with open(array_file, 'wb') as f:
        pickle.dump(image_arr, f)

# 从文件读取一维数组并恢复为图片

def file_to_image(array_file, result_path):
    with open(array_file, 'rb') as f:
        image_arr = pickle.load(f)
    
    # 获取原始图片的尺寸
    img = Image.open(image_path)
    width, height = img.size
    total_pixels = width * height
    
    # 将一维数组转换回三色数组
    r_arr = image_arr[:total_pixels].reshape(height, width) # 从一维数组重新塑造为二维数组
    g_arr = image_arr[total_pixels:2*total_pixels].reshape(height, width)
    b_arr = image_arr[2*total_pixels:].reshape(height, width)
    
    # 将三色数组转换回图像
    r = Image.fromarray(r_arr.astype(np.uint8)).convert('L')# astype(np.uint8) 将 r_arr 中的元素类型转换为 uint8（无符号8位整数 0-255）,Image.fromarray 是 Pillow 库中的一个方法，用于从 NumPy 数组创建一个图像对象。.convert('L') 是将图像对象转换为灰度图像模式
    g = Image.fromarray(g_arr.astype(np.uint8)).convert('L')
    b = Image.fromarray(b_arr.astype(np.uint8)).convert('L')
    image = Image.merge('RGB', (r, g, b)) # 合并三个通道为RGB图片
    
    # 将图片保存到指定路径
    image.save(result_path)


# 将图片转换为一维数组并保存
image_to_array(image_path, array_file)

# 从文件读取一维数组并恢复为图片
file_to_image(array_file, result_path)










