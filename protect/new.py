from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class DriverFactory:

    @staticmethod
    def create_driver():
        """Create a Selenium WebDriver instance."""
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Optional: Run in headless mode for CI/CD
        options.add_argument("--incognito")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.maximize_window()
        return driver
