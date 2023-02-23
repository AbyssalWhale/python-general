# pipenv install selenium
# pipe install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

BROWSER = webdriver.Chrome()
BROWSER.get("https://github.com/")
BROWSER.find_element(
    By.XPATH, "//button[contains(@class, 'signup')]").click()

assert "Welcome to GitHub!" in BROWSER.page_source

LABEL = BROWSER.find_element(
    By.XPATH, "//div[@id='email-container']//label[@class='text-mono signup-text-prompt']")
assert "Enter your email" in LABEL.text

BROWSER.quit()
