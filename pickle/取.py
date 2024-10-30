import pickle # 将文件存为二进制，然后随用随取
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
from PIL import Image



with open('./pickle_file.pkl','rb') as f: # rb: 读二进制， pickle_file.pkl二进制保存的文件
    [img,str1]=pickle.load(f)
img.show()
print(str1)