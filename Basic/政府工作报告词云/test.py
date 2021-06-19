import jieba
import wordcloud
from scipy.misc import imread
mask=imread("aixin.jpg")
f=open("test.txt","r",encoding="utf-8")
t=f.read()
f.close

w=wordcloud.WordCloud(font_path="msyh.ttf",mask=mask,\
        width=100,height=70,background_color="white",\
            )
w.generate("".join(jieba.lcut(t)))
w.to_file("wordcloud-1.png")
