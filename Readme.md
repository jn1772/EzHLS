#### EzHLS is a Simple and Quick command line based interactive utility written in python to get single media file out of a HLS m3u8 master playlist file link.

>**What does it do?**

**Input: master m3u8 playlist**  
**Output: combined (video+audio) media file from chunks**

Chunks are downloaded parallely (threads are configurable).
Once downloaded the data is passed to ffmpeg binary to generate the resulting media file.

>Prerequisites:
1. Need to have ffmpeg installed and binary available in PATH.

It assumes there will be a video and audio list in the master playlist and will ask user to select one from each video and audio list, giving him the resulting media file using ffmpeg.

>TODO:
1. Resume support/better failure handling.
2. More m3u8 options to user and support for them.
