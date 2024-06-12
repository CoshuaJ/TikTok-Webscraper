# TikTok Webscrape & Downloader

## Installation
- Clone repository
- [Optional] Create virtual env for packages [$ python -m venv .venv]
- Install requirements [$ pip install -r requirements.txt]

## Usage

### download.py
Intended for batch downloading Favourites, requires access to your TikTok user_data.json.
See https://support.tiktok.com/en/account-and-privacy/personalized-ads-and-data/requesting-your-data

- Place your TikTok user_data.json in the root directory
- Run download.py
- Extracts URLs from user_data.json and batch downloads them using yt-dlp

### scrape.py
Intended for obtaining the URLs of a TikTok collection (not possible using user_data.json as of Jan 2024) or any other profile page, which can then be batch downloaded using yt-dlp.

- Replace the 'link' variable on Line 6 with your desired page URL (for collections this requires sharing the collection from mobile)
- Run scrape.py
- You may be required to complete a captcha and/or login depending on the accessibility of the page
- Scrapes video URLs and places them into a links.txt file
- These links can then be batch downloaded from command line [$ yt-dlp -a links.txt] or using a similar approach to download.py
