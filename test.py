from selenium import webdriver

# Safari doesn't require options or external driver managers
driver = webdriver.Safari()

print("CI/CD is working!")

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

print("Page title is:", driver.title)
driver.quit()