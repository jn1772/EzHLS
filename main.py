import subprocess

from download_util import *
from m3u8_util import *
from user_util import *

if __name__ == "__main__":
    m3u8_url = ask_user_for_m3u8_url()
    final_file_name = ask_user_for_final_file_name()
    content_location = ask_user_for_content_location()
    m3u8_disk_location = save_playlist_from_url(m3u8_url, content_location)
    m3u8_loaded = load_playlist_from_url(m3u8_url)
    user_selections = ask_user_for_playlist(m3u8_loaded)

    video_m3u8_uri = user_selections[0].absolute_uri
    audio_m3u8_uri = user_selections[1].absolute_uri

    video_m3u8 = load_playlist_from_url(video_m3u8_uri)
    audio_m3u8 = load_playlist_from_url(audio_m3u8_uri)

    video_chunk_location = "{}/{}".format(content_location, "video")
    audio_chunk_location = "{}/{}".format(content_location, "audio")

    video_m3u8_file_location = "{}/{}".format(video_chunk_location, "video.m3u8")
    audio_m3u8_file_location = "{}/{}".format(audio_chunk_location, "audio.m3u8")

    download_files(video_m3u8, video_chunk_location)
    download_files(audio_m3u8, audio_chunk_location)

    video_m3u8.dump(video_m3u8_file_location)
    audio_m3u8.dump(audio_m3u8_file_location)

    video_file_name = "video_out.mp4"
    audio_file_name = "audio_out.aac"
    target_file_name = "{}.mp4".format(final_file_name)

    video_out_absolute_location = "{}/{}".format(content_location, video_file_name)
    audio_out_absolute_location = "{}/{}".format(content_location, audio_file_name)
    merged_out_absolute_location = "{}/{}".format(content_location, target_file_name)

    subprocess.run(["ffmpeg", "-y", "-protocol_whitelist", "file,http,https,tls,tcp", "-i", video_m3u8_file_location, "-c", "copy", video_out_absolute_location])
    subprocess.run(["ffmpeg", "-y", "-protocol_whitelist", "file,http,https,tls,tcp", "-i", audio_m3u8_file_location, "-c", "copy", audio_out_absolute_location])
    subprocess.run(["ffmpeg", "-y", "-i", video_out_absolute_location, "-i", audio_out_absolute_location, "-c", "copy", merged_out_absolute_location])
    print("done")

