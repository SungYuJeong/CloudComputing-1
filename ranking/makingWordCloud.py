#!/usr/bin/env python3

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from threading import Thread
from time import sleep

def making_wc():
    while True:
        font_path = '/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf'
        wordcloud = WordCloud(
            background_color='#ffffff',
            font_path = font_path,
            width = 1000,
            height = 500,
            colormap="nipy_spectral"
        )

        text=open('output.txt').read()
        wordcloud = wordcloud.generate(text)

        fig = plt.figure(figsize=(10,5))
        plt.imshow(wordcloud, interpolation="bilinear", aspect="auto")
        plt.axis("off")
        plt.show()
        fig.savefig('/home/ubuntu/project/CloudComputing/CloudComputing/page/projectPage/img/wordcloud.png',dpi=800)

    sleep(3600)
#================================================




def main():
    th = Thread(target=making_wc)
    th.demon = True
    th.start()


if __name__ == '__main__':
    main()
