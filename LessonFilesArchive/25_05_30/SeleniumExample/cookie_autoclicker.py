# This program will use selenium to automatically click on the cookie clicker webpage
# should serve as a motivation for my programming class students to show powers we have as programmers

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # NEW
from selenium.webdriver.common.by import By  # NEW
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Specify the path to ChromeDriver
service = Service("/Users/janhartman/24-25-python/25_05_30/SeleniumExample/chromedriver")  # e.g., "/Users/janhartman/Downloads/chromedriver"

# Start the browser
driver = webdriver.Chrome(service=service,options=options)

# Execute JavaScript to remove automation flag
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
    """
})

driver.get('https://orteil.dashnet.org/cookieclicker/')

time.sleep(1)

print("click1")

consent_button = driver.find_element(By.CSS_SELECTOR, "p.fc-button-label")
if consent_button.text == "Consent":
    consent_button.click()

time.sleep(1)
print("click2")

language_button = driver.find_element(By.CSS_SELECTOR, "div.langSelectButton")
print(language_button.text)
language_button.click()

# Wait some time so I can verify that I am not a robot
time.sleep(5)

cookie_button = driver.find_element(By.ID,"bigCookie")

while True:
    cookie_button.click()
    print("click")
    time.sleep(0.01)

driver.quit()