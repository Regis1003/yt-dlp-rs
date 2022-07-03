#!/usr/bin/bash

set -e
set -o pipefail

# Install dependencies
sudo apt-get update && apt-get upgrade
sudo apt-get install -y ffmpeg

# Downoad files and add to bin directory
sudo wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
