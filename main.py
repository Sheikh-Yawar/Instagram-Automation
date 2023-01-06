import getpass
import time
import os
import wget
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


userName = input("Enter your instagram username: ")
print("Enter your instagram password: ")
password = getpass.getpass()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)

driver.get("https://www.instagram.com/")

driver.quit()
time.sleep(2)

field1 = driver.find_element(
    By.XPATH, '//input[@name = "username"]')
field1.send_keys(userName)
field1.send_keys(Keys.ENTER)

field2 = driver.find_element(
    By.XPATH, '//input[@name = "password"]')
field2.send_keys(password)
field2.send_keys(Keys.ENTER)


time.sleep(3)
driver.implicitly_wait(5)


not_now = driver.find_element(
    By.XPATH, "//button[text() = 'Not Now']")
not_now.click()

time.sleep(2)
driver.implicitly_wait(5)

notifications_turnOff = driver.find_element(
    By.XPATH, "//button[text() = 'Not Now']")
notifications_turnOff.click()


print("Wolaa! You're logged in!")
search_username = input("Enter the username of the person: ")
os.mkdir(f'./Projects/instaAutomation/{search_username}')
time.sleep(2)
search_svg = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a')

search_svg.click()
time.sleep(1)

search_input = driver.find_element(
    By.XPATH, '//input[@aria-label = "Search input"]')
search_input.clear()
search_input.send_keys(search_username)

time.sleep(2)
search_input.send_keys(Keys.ENTER)
search_input.send_keys(Keys.ENTER)


time.sleep(5)
last_height = 0
my_images = set()
while True:
    images = driver.find_elements(
        By.XPATH, '//img[@class = "x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3"]')
    for image in images:
        source = image.get_attribute('src')
        my_images.add(source)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

print(len(my_images))


dest_loc = f'./Projects/instaAutomation/{search_username}'
for image in my_images:
    wget.download(image, dest_loc)
