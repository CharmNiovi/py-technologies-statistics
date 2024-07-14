from selenium.webdriver import Chrome, ChromeOptions


class CustomChrome(Chrome):
    def __init__(self):
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        super().__init__(options=options)
