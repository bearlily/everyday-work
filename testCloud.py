import jieba
from matplotlib import pyplot as plt
import wordcloud
from PIL import Image
import numpy as np
import sqlite3
import stopwords

con=sqlite3.connect('movie.db')
cur=con.cursor()
sql='select introduction from movie250'
data=cur.execute(sql)
text=""
for item in data:
    text=text+item[0]
# print(text)
cur.close()
con.close()

cut=jieba.cut(text)
string=' '.join(cut)
print(len(string))

img = Image.open(r'.\tree.jpg')
img_array = np.array(img)
wc=wordcloud.WordCloud(
    background_color='white',
    mask=img_array,
    font_path='boxicons.ttf'
).generate_from_text(string)

fig=plt.figure(1)
plt.imshow(wc)
plt.axis('off')

plt.show()














