import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re





def count_words(titles_list, stop_words):
    word_count = {}
    for title in titles_list:
        title_words = title.split()
        for word in title_words:
            word = word.upper()
            if word not in stop_words and re.match("\w", word):
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count


def make_word_cloud(word_count, channel):
    wc = WordCloud(background_color="white", width=1800, height=1200).generate_from_frequencies(word_count)
    plt.imshow(wc)
    plt.title(channel.capitalize(), fontsize=50, pad=20)
    plt.axis("off")
    plt.show()
