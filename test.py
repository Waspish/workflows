from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # for CI environments
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

print("Page title is:", driver.title)
driver.quit()