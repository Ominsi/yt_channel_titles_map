import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re


def find_all_titles(youtube, channel_name):
    response = youtube.channels().list(
        part="contentDetails",
        forUsername=channel_name
    ).execute()
    items = response.get("items")[0]
    content_details = items["contentDetails"]
    channel_playlists = content_details["relatedPlaylists"]
    uploads_id = channel_playlists["uploads"]
    playlist_length = youtube.playlists().list(
        part="contentDetails",
        id=uploads_id,
    ).execute().get("items")[0].get("contentDetails").get("itemCount")

    counter = 0
    next_page_token = ""
    titles = []
    while counter < playlist_length:
        if counter + 50 > playlist_length:
            result_amount = playlist_length - counter
        else:
            result_amount = 50

        uploads_playlist = youtube.playlistItems().list(
            part="snippet",
            playlistId=uploads_id,
            maxResults=result_amount,
            pageToken=next_page_token
        ).execute()
        next_page_token = uploads_playlist.get("nextPageToken")
        videos = uploads_playlist.get("items")
        for video in videos:
            titles.append(video.get("snippet").get("title"))
        counter += 50
    return titles


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
