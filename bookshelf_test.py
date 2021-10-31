import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait as wait
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
        login_page = page.LoginPage(self.driver)
        login_page.fill_username("testuser")
        login_page.fill_password("fxSkcKv^6gRxY@sj_bJDXWuqfGN=RnE+")
        login_page.click_login_button()
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
        bookstore_page.click_close_ads()
        bookstore_page.click_book('Git Pocket Guide')
        book_page = page.BookPage(self.driver)
        self.driver.execute_script('window.scrollBy(0,1000)')

        assert not book_page.is_add_button_exist(
        ), "Button to add book is on the page!"

        assert book_page.is_login_button_exist(
        ), "Button to login is not on the page!"

        book_page.click_login()
        self.driver.implicitly_wait(5)
        login_page = page.LoginPage(self.driver)
        login_page.fill_username("testuser")
        login_page.fill_password("fxSkcKv^6gRxY@sj_bJDXWuqfGN=RnE+")
        login_page.click_login_button()
        self.driver.implicitly_wait(5)

        assert book_page.is_add_button_exist(
        ), "Button to add book is not on the page!"

        assert not book_page.is_login_button_exist(
        ), "Button to login is on the page!"

        self.driver.implicitly_wait(5)
        self.driver.execute_script('window.scrollBy(0,1000)')

        book_page.click_add_book()
        self.driver.implicitly_wait(5)
        alert = wait(self.driver,
                     10).until(expected_conditions.alert_is_present())

        assert alert.text == 'Book added to your collection.', 'Book not added!'

        alert.accept()
        self.driver.implicitly_wait(5)

        assert book_page.is_add_button_exist(
        ), "Button to add book is not on the page!"

        assert not book_page.is_login_button_exist(
        ), "Button to login is on the page!"

        assert book_page.is_back_button_exist(
        ), "Button to back to store is not on the page!"

        book_page.click_add_book()
        self.driver.implicitly_wait(5)
        alert = wait(self.driver,
                     10).until(expected_conditions.alert_is_present())

        assert alert.text == 'Book already present in the your collection!', 'Book added!'

        alert.accept()
        self.driver.implicitly_wait(5)

        book_page.click_back()
        self.driver.implicitly_wait(5)
        book_page.click_close_ads()
        #book_page.click_profile()
        self.driver.get("https://demoqa.com/profile")
        self.driver.implicitly_wait(5)
        profile_page = page.ProfilePage(self.driver)
        self.driver.execute_script('window.scrollBy(0,1000)')

        assert profile_page.is_book_added(
            'Git Pocket Guide'), 'Book is not added!'

    def tearDown(self):
        self.driver.close()

    #fxSkcKv^6gRxY@sj_bJDXWuqfGN=RnE+


if __name__ == "__main__":
    unittest.main()