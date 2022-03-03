# Input of project packages
from setup_youtube_api import youtube_authenticate
from channel_titles import count_words, make_word_cloud
from api_handler import find_channel_id, find_all_titles
# Input of other packages
from stop_words import get_stop_words

if __name__ == '__main__':
    youtube = youtube_authenticate()
    channel_info = find_channel_id(youtube)
    titles = find_all_titles(youtube, channel_info[0])
    stop_words = [w.upper() for w in get_stop_words("en")]
    title_words = count_words(titles, stop_words)
    make_word_cloud(title_words, channel_info[1])

