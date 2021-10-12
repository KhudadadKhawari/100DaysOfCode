from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

USERNAME = 'your instagram username'
PASSWORD = 'your instgram password'
USERNAME_TO_FOLLOW_FOLLOWERS = 'user of someone u want to follow his/her followers'


options = Options()
options.add_argument("--start-maximized")
chrome_driver_path = "/home/khudadad/development/chromedriver_linux64/chromedriver"  # the webdriver path
driver = webdriver.Chrome(chrome_driver_path, options=options)

url = "https://instagram.com"
driver.get(url)
time.sleep(4)

username = driver.find_element_by_name("username")
username.send_keys(username)
password = driver.find_element_by_name("password")
password.send_keys(password)

login_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
login_btn.click()
time.sleep(6)


def get_followers_list():
    time.sleep(6)
    followers = driver.find_elements_by_css_selector("div li button")
    return followers


def get_updated_follower_list():
    followers = get_followers_list()
    followers[-1].click()
    time.sleep(2)
    try:
        cancel_btn = driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[2]")
        cancel_btn.click()
        time.sleep(2)
    except:
        print('waiting for 4 sec, cancel_follow button loading...')
        time.sleep(4)
    followers = get_followers_list()
    return followers


def follow_someone_followers(someone_username):
    total_followed = 0
    current_followed = 0
    driver.get(f"https://www.instagram.com/{someone_username}/")
    time.sleep(6)

    get_total_followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
    get_total_followers = str(get_total_followers.text)
    get_total_followers_text = get_total_followers.replace('k', '')
    get_total_followers_text = get_total_followers_text.replace('m', '')
    total_followers = int(get_total_followers_text) // 20
    print(f"Loop will Run [{total_followers}] times")
    time.sleep(2)

    show_followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    show_followers.click()
    time.sleep(4)

    for i in range(total_followers):
        followers = get_updated_follower_list()
        for follower in followers:
            if follower.text == 'Follow':
                follower.click()
                print('Following NOW')
                total_followed += 1
                current_followed += 1
                time.sleep(3)
            else:
                total_followed += 1
        if current_followed > 20:
            print(f'[10min] break \nFollowed: {current_followed} \nTotal:{total_followed}')
            time.sleep(600)
        current_followed = 0
        total_followed = 0


follow_someone_followers(USERNAME_TO_FOLLOW_FOLLOWERS)

