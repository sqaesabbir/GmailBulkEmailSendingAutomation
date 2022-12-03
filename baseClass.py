from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from config import EMAIL, PASSWORD
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.gmail.com")
email_input= driver.find_element(By.CSS_SELECTOR('input[type="email"]'));
email_input.send_keys(EMAIL);
email_input.is_displayed()