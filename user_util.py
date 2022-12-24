def ask_user_for_playlist(m3u8_playlist):
    for i in range(0, len(m3u8_playlist.playlists)):
        print("Playlist {}: {}\n".format(i, m3u8_playlist.playlists[i]))

    user_selected_video_track = int(input("Select Playlist Number"))

    audio_tracks = m3u8_playlist.playlists[user_selected_video_track].media

    for i in range(0, len(audio_tracks)):
        print("Audio Track {}: {}\n".format(i, audio_tracks[i]))

    user_selected_audio_track = int(input("Select Audio Track"))

    return [m3u8_playlist.playlists[user_selected_video_track], audio_tracks[user_selected_audio_track]]


def ask_user_for_m3u8_url():
    url = input("Paste master m3u8 url: ")
    return url

def ask_user_for_final_file_name():
    file_name = input("Final file name: ")
    return file_name

def ask_user_for_content_location():
    file_location = input("Content location (where to put output file): ")
    return file_location
