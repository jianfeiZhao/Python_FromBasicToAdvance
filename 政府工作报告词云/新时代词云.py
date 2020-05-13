import jieba
import wordcloud
from scipy.misc import imread
mask=imread("chinamap.jpg")
f=open("threekingdoms.txt","r",encoding="utf-8")
t=f.read()
f.close
ls=jieba.lcut(t)
txt="".join(ls)
w=wordcloud.WordCloud(font_path="msyh.ttf",mask=mask,\
        width=1000,height=700,background_color="white"  )
w.generate(txt)
w.to_file("wordcloud-2.png")
