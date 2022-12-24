import m3u8
import urllib.request
import os


def save_playlist_from_url(url, save_at):
    file_name = "playlist.m3u8"
    file_path = "{}/{}".format(save_at, file_name)
    if not os.path.isdir(save_at):
        os.makedirs(save_at)
    urllib.request.urlretrieve(url, file_path)
    return file_path


def load_playlist_from_url(location):
    res = m3u8.load(location)
    return res
