# Input of project packages
from setup_youtube_api import youtube_authenticate
from channel_titles import find_all_titles, count_words, make_word_cloud

# Input of other packages
from stop_words import get_stop_words

if __name__ == '__main__':
    channel_name = input("Channel Name: ").strip().lower()
    youtube = youtube_authenticate()
    titles = find_all_titles(youtube, channel_name)
    stop_words = [w.upper() for w in get_stop_words("en")]
    title_words = count_words(titles, stop_words)
    make_word_cloud(title_words, channel_name)

