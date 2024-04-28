from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:
    CHROME = 1
    FIREFOX = 2
    EDGE = 3

    @staticmethod
    def create_driver(driver_id: int, is_headless=False):
        match int(driver_id):
            case 1:
                chrome_options = Options()
                if is_headless:
                    chrome_options.add_argument('--headless')
                chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
                driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
            case 2:
                driver = webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()))
            case 3:
                driver = webdriver.Edge(service=EdgeService(executable_path=EdgeChromiumDriverManager().install()))
            case _:
                driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        return driver
