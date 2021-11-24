import pandas as pd
import collections
import wordcloud
import matplotlib.pyplot as plt
import PIL.Image as image
import numpy as np
ex=pd.read_excel('浦北中学各班同学线上补习账号及密码（高二）.xlsx')
name=list([i[0] for i in ex['姓名']])
n=collections.Counter(name)
print(n)
mask=np.array(image.open('heart.jpg'))
wc = wordcloud.WordCloud(
font_path='msyhbd.ttf', # 设置字体格式
mask=mask,#mask=mask, # 设置背景图
max_words=200, # 最多显示词数
max_font_size=80) # 字体最大值
wc.generate_from_frequencies(n)

#plt.figure(figsize=(18,8))
plt.imshow(wc)
plt.axis('off')
print(wc)
#plt.savefig('hhh.png')
plt.show()