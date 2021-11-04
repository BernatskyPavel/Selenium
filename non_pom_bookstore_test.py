import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.common.by import By
import page
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.relative_locator import locate_with


class DemoQA(unittest.TestCase):
    # Sample test case using POM
    def setUp(self):
        firefox_options = Options()
        # firefox_options.add_argument("--headless")
        # Для университетской сети
        PROXY = "172.16.0.101:3128"
        webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
            "httpProxy": PROXY,
            "sslProxy": PROXY,
            "noProxy": ["127.0.0.1"],
            "proxyType": "MANUAL",
        }
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com")

    def test_demoqa_login(self):
        self.driver.find_element(
            By.XPATH, "//*[@class='card mt-4 top-card'][6]").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, 'login').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, 'userName').send_keys("testuser")
        self.driver.find_element(By.ID, 'password').send_keys(
            "fxSkcKv^6gRxY@sj_bJDXWuqfGN=RnE+")
        self.driver.find_element(By.ID, 'login').click()
        self.driver.implicitly_wait(5)
        assert "testuser" not in self.driver.page_source, "Not logged!"
        self.driver.find_element(By.ID, 'submit').click()

    def test_books_list(self):
        self.driver.find_element(
            By.XPATH, "//*[@class='card mt-4 top-card'][6]").click()
        self.driver.implicitly_wait(5)
        self.assertEqual(len(self.driver.find_elements(By.CSS_SELECTOR, '.rt-tbody > .rt-tr-group > div a')),
                         8, "Number of books is not equal 8!")
        self.driver.execute_script('window.scrollBy(0,1000)')
        element = self.driver.find_element(By.CLASS_NAME, 'select-wrap')
        select_element = element.find_element(By.TAG_NAME, 'select')
        select_object = Select(select_element)
        select_object.select_by_value(str(5))
        self.driver.implicitly_wait(5)
        self.assertEqual(len(self.driver.find_elements(By.CSS_SELECTOR, '.rt-tbody > .rt-tr-group > div a')),
                         5, "Number of books is not equal 5!")
        element = self.driver.find_element(By.CLASS_NAME, '-next')
        button = element.find_element(By.TAG_NAME, 'button')
        button.click()
        self.assertEqual(len(self.driver.find_elements(By.CSS_SELECTOR, '.rt-tbody > .rt-tr-group > div a')),
                         3, "Number of books is not equal 3!")
        element = self.driver.find_element(By.CLASS_NAME, '-next')
        assert len(element.find_elements(
            By.XPATH, './button[@disabled]')) != 0, "There is one more page!"
        element = self.driver.find_element(By.CLASS_NAME, '-previous')
        button = element.find_element(By.TAG_NAME, 'button')
        button.click()
        self.assertEqual(len(self.driver.find_elements(By.CSS_SELECTOR, '.rt-tbody > .rt-tr-group > div a')),
                         5, "Number of books is not equal 5!")
        element = self.driver.find_element(By.CLASS_NAME, '-previous')
        assert len(element.find_elements(
            By.XPATH, './button[@disabled]')) != 0, "There is one more page!"

    def test_adding_book(self):
        self.driver.find_element(
            By.XPATH, "//*[@class='card mt-4 top-card'][6]").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, 'close-fixedban').click()
        self.driver.find_element(
            By.XPATH, f'//*[@id="see-book-Git Pocket Guide"]/a').click()
        self.driver.execute_script('window.scrollBy(0,1000)')
        assert not len(self.driver.find_elements(
            By.XPATH, "//*[@class='text-right fullButton']/button")) != 0, "Button to add book is on the page!"

        assert len(self.driver.find_elements(By.ID, 'login')
                   ) != 0, "Button to login is not on the page!"
        self.driver.find_element(By.ID, 'login').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, 'userName').send_keys("testuser")
        self.driver.find_element(By.ID, 'password').send_keys(
            "fxSkcKv^6gRxY@sj_bJDXWuqfGN=RnE+")
        self.driver.find_element(By.ID, 'login').click()
        self.driver.implicitly_wait(5)
        assert len(self.driver.find_elements(
            By.XPATH, "//*[@class='text-right fullButton']/button")) != 0, "Button to add book is on the page!"
        assert not len(self.driver.find_elements(By.ID, 'login')
                       ) != 0, "Button to login is not on the page!"
        self.driver.execute_script('window.scrollBy(0,1000)')
        self.driver.implicitly_wait(5)
        self.driver.find_element(
            By.XPATH, "//*[@class='text-right fullButton']/button").click()
        alert = wait(self.driver,
                     10).until(expected_conditions.alert_is_present())
        result = alert.text
        alert.accept()
        self.assertEqual(
            result, "Book added to your collection.", "Book added again!")
        self.driver.implicitly_wait(5)
        self.driver.find_element(
            By.XPATH, "//*[@class='text-right fullButton']/button").click()
        alert = wait(self.driver,
                     10).until(expected_conditions.alert_is_present())
        result = alert.text
        alert.accept()
        self.assertEqual(
            result, "Book already present in the your collection!", "Book added again!")
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.text-left.fullButton>button#addNewRecordButton').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, 'close-fixedban').click()
        self.driver.execute_script('window.scrollBy(0,1000)')
        elements = self.driver.find_elements(By.CSS_SELECTOR,
                                             'div.left-pannel>div.accordion>div.element-group')
        bookstore = elements[5].find_elements(
            By.CSS_SELECTOR, 'div.element-list>ul.menu-list>li')
        bookstore[2].click()
        self.driver.implicitly_wait(5)
        self.driver.execute_script('window.scrollBy(0,1000)')
        self.assertTrue(len(self.driver.find_elements(By.XPATH, f'//*[@id="see-book-Git Pocket Guide"]/a')
                            ), 'Book is missing!')
        self.driver.find_element(
            By.XPATH, f".//*[@id='see-book-Git Pocket Guide']/../../..//*[@id='delete-record-undefined']").click()
        modal = wait(self.driver,
                     10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'modal-dialog')))
        result = modal.find_element(By.CLASS_NAME, 'modal-body').text
        modal.find_element(By.ID, 'closeSmallModal-cancel').click()
        self.assertEqual(
            result, "Do you want to delete this book?", "Wrong delete message!")
        self.assertTrue(len(self.driver.find_elements(By.XPATH, f'//*[@id="see-book-Git Pocket Guide"]/a')
                            ), 'Book is missing!')
        self.driver.find_element(
            By.XPATH, f".//*[@id='see-book-Git Pocket Guide']/../../..//*[@id='delete-record-undefined']").click()
        modal = wait(self.driver,
                     10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'modal-dialog')))
        modal_text = modal.find_element(By.CLASS_NAME, 'modal-body').text
        modal.find_element(By.ID, 'closeSmallModal-ok').click()

        alert = wait(self.driver,
                     10).until(expected_conditions.alert_is_present())
        alert_text = alert.text
        alert.accept()
        self.assertEqual(
            modal_text, "Do you want to delete this book?", "Wrong delete message!")
        self.assertEqual(
            alert_text, "Book deleted.", "Wrong alert message!")
        self.driver.implicitly_wait(5)
        self.assertFalse(len(self.driver.find_elements(By.XPATH, f'//*[@id="see-book-Git Pocket Guide"]/a')
                             ), 'Book is presented!')
        self.driver.implicitly_wait(5)
        self.driver.execute_script('window.scrollBy(0,-1000)')
        nei = self.driver.find_element(By.ID, 'userName-value')
        self.assertTrue(len(self.driver.find_elements(locate_with(By.TAG_NAME, "button").to_right_of(nei))) != 0,
                        'Log out button is missing!')
        self.driver.find_element(locate_with(
            By.TAG_NAME, "button").to_right_of(nei)).click()
        self.driver.implicitly_wait(5)
        self.assertEqual(self.driver.current_url,
                         'https://demoqa.com/login', 'Logout fault!')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
