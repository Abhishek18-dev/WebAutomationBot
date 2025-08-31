# Trello Automation Bot (Selenium)

## 📌 About
This project automates Trello tasks using Python and Selenium.  
It has **two implementations**:

- **Dynamic Bot** → Uses `WebDriverWait` (smart waiting, reliable).  
- **Static Bot** → Uses `time.sleep()` (simple but less reliable).  

Both versions were created by **Abhishek** for **educational and ethical purposes only**.  
⚠️ Please do not misuse this bot. It is strictly meant for learning, personal productivity, and ethical automation.  

---

## ✨ Features
- Logs into Trello automatically.
- Navigates to a specified Trello board.
- Adds tasks/cards automatically.
- Saves screenshots for reference.
- Provides both dynamic and static approaches.


---


## ⚠️ Note

Trello’s UI may change in the future. If that happens, some parts of the bot (like selectors or XPaths) may need to be updated to continue working.

Always keep Chrome and ChromeDriver updated to the same version.

You can do the same for other websites , you just have do some UI changes which are relevent for that websites.

---

## 🔧 Requirements
- Python **3.8+**
- Google Chrome installed
- ChromeDriver (same version as your Chrome)

## Install dependencies
Create a file named `requirements.txt` with the following content:
```txt
selenium==4.23.1 

```Then install using:

pip install -r requirements.txt 


## 📂 Project Structure
.
├── dynamic_bot.py       # Dynamic version (recommended)
├── static_bot.py        # Static version
├── config.json          # Credentials and task details
├── requirements.txt     # Dependencies
├── downloads/
│   └── screenshots/     # Saved screenshots
└── README.md            # Documentation



## ⚙️Setup & Usage

Download/clone this repository.

Download ChromeDriver 

Place chromedriver.exe in the same folder as scripts.

Ensure its version matches your installed Chrome.

Create a file named config.json in the same folder and add your credentials:

{
    "USERNAME": "your_email@example.com",
    "PASSWORD": "your_password",
    "BOARD_NAME": "Your Trello Board Name",
    "TASK_NAME": "Your Task to Add"
}


## 👤 Author
Created by: Abhishek

For: Students, developers, and learners who want to explore Selenium automation.

⚠️ Disclaimer
This project is for educational and ethical purposes only.
Do not misuse it for spamming, hacking, or violating Trello’s terms of service.
The author (Abhishek) holds no responsibility for any unethical use of this code.
