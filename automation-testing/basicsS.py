# pipenv install selenium
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://github.com/"
SIGNUP_BUTTON = "//button[contains(@class, 'signup')]"
ENTEREMAIL_LABEL = "//div[@id='email-container']//label[@class='text-mono signup-text-prompt']"

BROWSER = webdriver.Chrome()
BROWSER.get(URL)
BROWSER.find_element(
    By.XPATH, SIGNUP_BUTTON).click()

assert "Welcome to GitHub!" in BROWSER.page_source

LABEL = BROWSER.find_element(
    By.XPATH, ENTEREMAIL_LABEL)
assert "Enter your email" in LABEL.text

BROWSER.quit()
