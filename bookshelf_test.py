import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import page
import time


class DemoQA(unittest.TestCase):
    #Sample test case using POM
    def setUp(self):
        firefox_options = Options()
        #firefox_options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=firefox_options)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com")

    def test_demoqa_login(self):
        #Visits apress.com
        home_page = page.HomePage(self.driver)
        home_page.click_bookstore_menu()

        bookstore_page = page.BookStorePage(self.driver)
        bookstore_page.click_login_button()
        bookstore_page.fill_username("testuser")
        bookstore_page.fill_password("fxSkcKv^6gRxY@sj_bJDXWuqfGN=RnE+")
        bookstore_page.click_login_button()
        self.driver.implicitly_wait(5)
        #Checks if page is not empty
        assert bookstore_page.check_is_logged(), "Not logged!"

        bookstore_page.click_logout_button()

    def test_books_list(self):
        home_page = page.HomePage(self.driver)
        home_page.click_bookstore_menu()
        bookstore_page = page.BookStorePage(self.driver)
        self.driver.implicitly_wait(5)

        assert bookstore_page.check_books_number(
            8), "Number of books is not equal 8!"

        self.driver.execute_script('window.scrollBy(0,1000)')
        bookstore_page.change_page_size(5)
        self.driver.implicitly_wait(5)

        assert bookstore_page.check_books_number(
            5), "Number of books is not equal 5!"

        bookstore_page.click_next_page_button()

        assert bookstore_page.check_books_number(
            3), "Number of books is not equal 3!"

        assert bookstore_page.check_no_next_page(), "There is one more page!"

        bookstore_page.click_prev_page_button()

        assert bookstore_page.check_books_number(
            5), "Number of books is not equal 5!"

        assert bookstore_page.check_no_prev_page(), "There is one more page!"

    def test_adding_book(self):
        home_page = page.HomePage(self.driver)
        home_page.click_bookstore_menu()
        bookstore_page = page.BookStorePage(self.driver)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.close()

    #fxSkcKv^6gRxY@sj_bJDXWuqfGN=RnE+


if __name__ == "__main__":
    unittest.main()