import json
import subprocess
import os
import sys
import re

# read JSON
# https://support.tiktok.com/en/account-and-privacy/personalized-ads-and-data/requesting-your-data
with open("user_data.json", "r") as file:
    json_data = file.read()

# parse JSON
data = json.loads(json_data)

# extract links from the "Favorite Videos" section
favorite_videos = data["Activity"]["Favorite Videos"]["FavoriteVideoList"]
video_links = [video["Link"] for video in favorite_videos]

# file path to yt-dlp exe
yt_dlp_path = os.path.join(sys.prefix, "bin", "yt-dlp")
output_dir = "videos"
output_template = "%(id)s.%(ext)s"

# check if video already exists (via video ID), avoid redownloading existing videos
def video_exists(link, videos_directory="videos"):
    # Extract video ID from the link using a regular expression
    video_id_match = re.search(r'/video/(\d+)/', link)

    if video_id_match:
        video_id = video_id_match.group(1)
        video_file_path = os.path.join(videos_directory, f"{video_id}.mp4")

        # Check if the file already exists
        return os.path.exists(video_file_path)
    else:
        print(f"Could not extract video ID from {link}. Skipping.")
        return False

for link in video_links:
    if video_exists(link):
        print(f"Skipping download for {link}. File already exists.")
    else:
        print(f"Downloading: {link}")
        command = [yt_dlp_path, link, "-o", output_template]
        subprocess.run(command)
