from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import date
import os
import json

CHROME_DRIVER_PATH = os.path.join(os.getcwd(),"chromedriver.exe")

OP = webdriver.ChromeOptions()
#OP.add_argument("--headless")
#OP.add_argument("--disable-gpu")

quiet_mode = True
if quiet_mode:
    OP.add_experimental_option("excludeSwitches", ["enable-logging"])
    OP.add_argument("--log-level=3")

service = Service(executable_path =CHROME_DRIVER_PATH)
DRIVER = webdriver.Chrome(service = service , options=OP)

def screenshotPage():
    time.sleep(2)
    date_str = date.today().strftime("%d-%m-%Y_%H-%M-%S")
    file_path = os.path.join(os.getcwd() , 'downloads/screenshots/{}.png'.format(date_str))
    # ensure folder exists if not then create it
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    DRIVER.save_screenshot(file_path)
    print(f"Screenshot saved at: {file_path}")


def login():
    with open("config.json") as configFile:
        credentials = json.load(configFile)
        #print(credentials)
        time.sleep(2)
        #DRIVER.find_element(By.XPATH, value = "//a[@href = 'https://id.atlassian.com/login?application=trello&amp;continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3Fdisplay%3DeyJ2ZXJpZmljYXRpb23TdHJhdGVneSI6InNvZnQifQ%233D%233D&amp;display=eyJ2ZXJpZmljYXRpb23TdHJhdGVneSI6InNvZnQifQ%3D%3D']").click()
        #xpath method not working
        DRIVER.find_element(By.LINK_TEXT, value = "Log in").click()
        time.sleep(6)
        username = DRIVER.find_element(By.CSS_SELECTOR,"input[name = 'username']")
        time.sleep(3)
        username.clear()
        time.sleep(3)
        username.send_keys(credentials["USERNAME"])
        time.sleep(3)

        DRIVER.find_element(By.ID, value = "login-submit").click()
        time.sleep(3)

        password = DRIVER.find_element(by=By.CSS_SELECTOR,value="input[name = 'password']")
        time.sleep(3)
        password.clear()
        time.sleep(3)
        password.send_keys(credentials["PASSWORD"])
        time.sleep(3)

        DRIVER.find_element(By.ID,value="login-submit").click()
        time.sleep(16)


def navigate_to_board(boardname):
    time.sleep(5)
    DRIVER.find_element(By.XPATH,value="//a[@title='{}']".format(boardname)).click()
    time.sleep(5)


def addTask():
    with open("config.json") as configFile:
        credentials = json.load(configFile)
        time.sleep(2)
        #DRIVER.find_element(By.XPATH, value="//a[@title='Add a card']").click()
        DRIVER.find_element(By.XPATH, value="//button[text()='Add a card']").click()
        time.sleep(2)
        taskName = DRIVER.find_element(By.XPATH, value="//textarea[@placeholder='Enter a title or paste a link']")
        taskName.clear()
        time.sleep(2)
        taskName.send_keys(credentials["TASK_NAME"])
        time.sleep(2)
        DRIVER.find_element(By.XPATH, value="//button[@aria-label='Add card in To Do']").click()
        time.sleep(5)



def main():
    if not os.path.exists(CHROME_DRIVER_PATH):
        print("ChromeDriver not found at:", CHROME_DRIVER_PATH)
        exit()

    try:
        with open("config.json") as configFile:
            credentials = json.load(configFile)

        url = "https://trello.com"
        DRIVER.get(url)
        login()
        navigate_to_board(credentials["BOARD_NAME"])
        # Add your bot operations here
        addTask() # yaha se bhejne wala banao
        screenshotPage()
        input("Bot operation completed . Press any key to close Trello tab")
        DRIVER.close()
    except Exception as e:
        print(f"error occured in opening url : {url} as "  + str(e))
        DRIVER.close()

if __name__ == "__main__":
    main()