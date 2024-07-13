from selenium.webdriver import Chrome, ChromeOptions


def get_chrome_driver() -> Chrome:
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    return Chrome(options=options)
