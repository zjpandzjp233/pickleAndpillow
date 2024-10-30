import pickle # 将变量存为二进制，然后随用随取
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
from PIL import Image
img=Image.open('./微信图片_20240613144845.jpg')
str1="1235a498e4g3w1eg98eg4g\na64g9a8weg13a1dsg651ae9w8g1a531g89ad4sg6aer1haer8h4a9er8ha65er4y46429548445-y+*//-o/"

with open('./pickle_file.pkl','wb') as f: # wb: 写二进制， pickle_file.pkl二进制保存的文件
    pickle.dump([img,str1],f)