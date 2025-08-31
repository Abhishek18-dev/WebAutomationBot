from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import os
import json


CHROME_DRIVER_PATH = os.path.join(os.getcwd(),"chromedriver.exe")

OP = webdriver.ChromeOptions()
# Run Chrome in headless mode (browser runs in background, no window is shown)
#OP.add_argument("--headless=new")

# Disable GPU hardware acceleration (often needed for headless mode; optional for modern versions)
#OP.add_argument("--disable-gpu")


quiet_mode = True
if quiet_mode:
    OP.add_experimental_option("excludeSwitches", ["enable-logging"])
    OP.add_argument("--log-level=3")

service = Service(executable_path =CHROME_DRIVER_PATH)
DRIVER = webdriver.Chrome(service = service , options=OP)

#### Function to take a screenshot of the page
def screenshotPage():
    time.sleep(2)
    timestrap = datetime.today().strftime("%d-%m-%Y_%H-%M-%S-%f")
    file_path = os.path.join(os.getcwd() , 'downloads/screenshots/taskadded_{}.png'.format(timestrap))
    # ensure folder exists if not then create it
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    DRIVER.save_screenshot(file_path)
    print(f"Screenshot saved at: {file_path}")

#### Function to Log in to Trello website
def login(username, password):
        
        #DRIVER.find_element(By.XPATH, value = "//a[@href = 'https://id.atlassian.com/login?application=trello&amp;continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3Fdisplay%3DeyJ2ZXJpZmljYXRpb23TdHJhdGVneSI6InNvZnQifQ%233D%233D&amp;display=eyJ2ZXJpZmljYXRpb23TdHJhdGVneSI6InNvZnQifQ%3D%3D']").click()
        #xpath method not working

        #Used to click on Login button
        login_button_locator = (By.LINK_TEXT, "Log in")
        # Wait till button is clickable
        WebDriverWait(DRIVER, 10).until(
            EC.element_to_be_clickable(login_button_locator)
        )
        login_button = DRIVER.find_element(*login_button_locator)
        login_button.click()


        # Wait for username field to be visible and input credentials
        username_locator = (By.CSS_SELECTOR, "input[name='username']")
        WebDriverWait(DRIVER, 10).until(
            EC.visibility_of_element_located(username_locator)   # 👈 sahi choice
        )
        username_field = DRIVER.find_element(*username_locator)
        username_field.send_keys(username)


        #Used to submit user login
        user_submit_button_locator = (By.ID, "login-submit")

        WebDriverWait(DRIVER, 10).until(
            EC.element_to_be_clickable(user_submit_button_locator)
        )
        user_submit_button = DRIVER.find_element(*user_submit_button_locator)
        user_submit_button.click()


        # Wait for password field to be visible and input credentials
        password_locator = (By.CSS_SELECTOR, "input[name='password']")
        WebDriverWait(DRIVER, 10).until(
            EC.visibility_of_element_located(password_locator)   # 👈 sahi choice
        )
        password_field = DRIVER.find_element(*password_locator)
        password_field.send_keys(password)

        # Used to click on main login button
        main_login_button_locator = (By.ID, "login-submit")
        WebDriverWait(DRIVER, 10).until(
            EC.element_to_be_clickable(main_login_button_locator)
        )
        main_login_button = DRIVER.find_element(*main_login_button_locator)
        main_login_button.click()
        screenshotPage()


#### Find the board link using its title
def navigate_to_board(boardname):
    board_locator = (By.XPATH, f"//a[@title='{boardname}']")

    # Wait until board link is clickable
    WebDriverWait(DRIVER, 10).until(
        EC.element_to_be_clickable(board_locator)
    )
    board = DRIVER.find_element(*board_locator)
    board.click()
    screenshotPage()
    

#### Function to add a task to the board
def addTask(task_name):

        # Wait for "Add a card" button and click
        add_card_button_locator = (By.XPATH, "//button[text()='Add a card']")
        WebDriverWait(DRIVER, 10).until(
            EC.element_to_be_clickable(add_card_button_locator)
        )
        DRIVER.find_element(*add_card_button_locator).click()

        # Wait for task input field and enter task name
        taskName_input_locator = (By.XPATH, "//textarea[@placeholder='Enter a title or paste a link']")
        WebDriverWait(DRIVER, 10).until(
            EC.visibility_of_element_located(taskName_input_locator)
        )
        taskName_input = DRIVER.find_element(*taskName_input_locator)
        taskName_input.clear()
        taskName_input.send_keys(task_name)

        # Wait for "Add card" button and click
        addCardInToDo_button_locator = (By.XPATH, "//button[@aria-label='Add card in To Do']")
        WebDriverWait(DRIVER, 10).until(
            EC.element_to_be_clickable(addCardInToDo_button_locator)
        )
        DRIVER.find_element(*addCardInToDo_button_locator).click()


#### Function to manage the main workflow
def main():
    if not os.path.exists(CHROME_DRIVER_PATH):
        print("ChromeDriver not found at:", CHROME_DRIVER_PATH)
        exit()

    try:
        with open("config.json") as configFile:
            credentials = json.load(configFile)

        url = "https://trello.com"
        DRIVER.get(url)
        login(credentials["USERNAME"], credentials["PASSWORD"])
        navigate_to_board(credentials["BOARD_NAME"])
        addTask(credentials["TASK_NAME"]) # Mention the task in config.json you want to add
        screenshotPage()
        input("bot operation completed . Press any key to close trello tab")
        DRIVER.quit()
    except Exception as e:
        print(f"error occured in opening url : {url} as "  + str(e))
        screenshotPage()

#### Entry point for the script
if __name__ == "__main__":
    main()