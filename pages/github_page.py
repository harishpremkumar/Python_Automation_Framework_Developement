from selenium.webdriver.common.by import By

class GitHubPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://github.com"
    
    def open(self):
        """Open GitHub homepage."""
        self.driver.get(self.url)
        self.driver.maximize_window()
    
    def get_page_source(self):
        """Return the page source of the current webpage."""
        return self.driver.page_source
    
    def get_word_count(self, word):
        """Count occurrences of a word in the page source."""
        page_source = self.get_page_source()
        return page_source.count(word)
