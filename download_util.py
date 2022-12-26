import threading
import urllib.request
import os
from multiprocessing.pool import ThreadPool

total = 0
done = 0
lock = threading.Lock()


def update_progress_increase_by_one():
    global total, done
    with lock:
        done = done + 1
    print("Progress : {} % {}/{}".format((done * 100) / total, done, total))


def download(uri, disk_location):
    for i in range(0, 10):
        try:
            request = urllib.request.urlopen(uri, timeout=120)
            with open(disk_location, 'wb') as f:
                try:
                    f.write(request.read())
                except Exception as e:
                    print("Error writing chunk {} to disk. {}\n".format(uri, e))
                    continue
            update_progress_increase_by_one()
        except Exception as e:
            print(
                "Failed to download chunk {} attempt {} at address {} due to {}\n".format(disk_location, i + 1, uri, e))
            continue
        break


def download_parallel(uris, disk_location, thread_count=6):
    args = []
    for i in range(0, len(uris)):
        args.append((uris[i], disk_location[i]))
    with ThreadPool(thread_count) as pool:
        map_result = pool.starmap_async(download, args)
        map_result.get()
        pool.close()


def download_files(m3u8_video, disk_location):
    global total, done
    if not os.path.isdir(disk_location):
        os.makedirs(disk_location)
    done = 0
    segment_list = m3u8_video.segments
    total = len(segment_list)
    download_parallel([segment.absolute_uri for segment in segment_list],
                      ["{}/{}".format(disk_location, segment.uri) for segment in segment_list])
