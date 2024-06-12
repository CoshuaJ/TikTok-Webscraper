from selenium import webdriver
from bs4 import BeautifulSoup
import time

# EXAMPLE LINK, replace with your own
link = "https://www.tiktok.com/@papayaho.cat?lang=en" 

chrome_options = webdriver.ChromeOptions()
#TODO: use chrome cookies
#chrome_profile_path = ""
#chrome_options.add_argument("--user-data-dir=" + chrome_profile_path)

driver = webdriver.Chrome(options=chrome_options)
driver.get(link)
# let browser load
time.sleep(3)
# check for captcha/login
wait = input("Complete captcha & sign-in (if required), then press Enter to run: ")

soup = BeautifulSoup(driver.page_source, "html.parser")
# select div class that contains videos
videos = soup.find_all("div", {"class": "css-vi46v1-DivDesContainer eih2qak4"})
print(len(videos))
if len(videos) > 0:
    with open("links.txt", "w") as file:
        for video in videos:
            file.write(video.a["href"] + "\n")
            
