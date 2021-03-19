from selenium import webdriver

chrome_path = "./chromedriver"
siteUrl = "choongang.riroschool.co.kr"
userID = "20-10318"
UserPW = "tyty12528"

wd = webdriver.Chrome(executable_path=chrome_path)
wd.get(url=siteUrl)