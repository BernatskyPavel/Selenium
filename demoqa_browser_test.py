import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import page
import time


class DemoQA(unittest.TestCase):
    # Sample test case using POM
    def setUp(self):
        # firefox_options = Options()
        # firefox_options.add_argument("--headless")
        # Для университетской сети
        # PROXY = "172.16.0.101:3128"
        # webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
        #     "httpProxy": PROXY,
        #     "sslProxy": PROXY,
        #     "noProxy": ["127.0.0.1"],
        #     "proxyType": "MANUAL",
        # }
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com")

    def test_demoqa_main(self):
        self.driver.implicitly_wait(5)
        assert self.driver.current_url == 'https://demoqa.com/', 'Wrong page!'
        assert self.driver.title == 'DEMOQA', 'Wrong title!'

        self.driver.get('https://www.toolsqa.com/selenium-training/')
        self.driver.implicitly_wait(5)

        assert self.driver.current_url == 'https://www.toolsqa.com/selenium-training/', 'Wrong page!'
        assert self.driver.title == 'Tools QA - Selenium Training', 'Wrong title!'

        self.driver.back()
        self.driver.implicitly_wait(5)

        assert self.driver.current_url == 'https://demoqa.com/', 'Wrong page!'
        assert self.driver.title == 'DEMOQA', 'Wrong title!'

        self.driver.forward()
        self.driver.implicitly_wait(5)

        assert self.driver.current_url == 'https://www.toolsqa.com/selenium-training/', 'Wrong page!'
        assert self.driver.title == 'Tools QA - Selenium Training', 'Wrong title!'

        original = self.driver.current_window_handle

        self.driver.switch_to.new_window('tab')

        self.driver.get('https://demoqa.com/')
        self.driver.implicitly_wait(5)

        assert self.driver.current_url == 'https://demoqa.com/', 'Wrong page!'
        assert self.driver.title == 'DEMOQA', 'Wrong title!'

        self.driver.close()
        self.driver.switch_to.window(original)
        self.driver.implicitly_wait(5)

        assert self.driver.current_url == 'https://www.toolsqa.com/selenium-training/', 'Wrong page!'
        assert self.driver.title == 'Tools QA - Selenium Training', 'Wrong title!'

        time.sleep(2)
        self.driver.set_window_size(800, 600)
        assert self.driver.get_window_size().get("width") == 800, 'Wrong width!'
        assert self.driver.get_window_size().get("height") == 600, 'Wrong height!'

        time.sleep(2)
        self.driver.set_window_position(100, 100)
        assert self.driver.get_window_position().get("x") == 100, 'Wrong x value!'
        assert self.driver.get_window_position().get("y") == 100, 'Wrong y value!'

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
