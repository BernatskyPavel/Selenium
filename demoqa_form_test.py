import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait as wait
import page
import time
from datetime import date

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

    def test_demoqa_form(self):
        home_page = page.HomePage(self.driver)
        home_page.click_forms_menu()
        assert self.driver.current_url, "https://demoqa.com/forms"
        self.driver.implicitly_wait(5)
        home_page.click_close_ads()
        self.assertTrue(home_page.is_menu_opened(home_page.Menus.FORMS))
        home_page.click_left_menu(home_page.Menus.FORMS)
        self.assertTrue(not home_page.is_menu_opened(home_page.Menus.FORMS))

    def test_demoqa_form_open(self):
        home_page = page.HomePage(self.driver)
        home_page.click_forms_menu()
        self.assertEqual(self.driver.current_url, "https://demoqa.com/forms")
        time.sleep(2)
        home_page.click_close_ads()
        self.assertTrue(home_page.is_menu_opened(home_page.Menus.FORMS))
        home_page.click_practice_form()
        self.assertEqual(self.driver.current_url, "https://demoqa.com/automation-practice-form")
        
    def test_demoqa_form_simple_inputs(self):
        home_page = page.HomePage(self.driver)
        home_page.click_forms_menu()
        time.sleep(2)
        home_page.click_close_ads()
        home_page.click_practice_form()
        practice_form_page = page.PracticeFormPage(self.driver)
        practice_form_page.send_form()
        self.assertFalse(practice_form_page.is_form_sended())
        practice_form_page.input_name("Name")
        practice_form_page.input_lastname("LastName")
        selected = practice_form_page.select_gender("Wrong")
        self.assertFalse(selected)
        selected = practice_form_page.select_gender("Male")
        self.assertTrue(selected)
        practice_form_page.input_mobile("wrong")
        practice_form_page.send_form()
        self.assertFalse(practice_form_page.is_form_sended())
        practice_form_page.input_mobile("1111222233")
        practice_form_page.send_form()
        self.assertTrue(practice_form_page.is_form_sended())

    def test_demoqa_form_all_inputs(self):
        home_page = page.HomePage(self.driver)
        home_page.click_forms_menu()
        time.sleep(2)
        home_page.click_close_ads()
        home_page.click_practice_form()
        practice_form_page = page.PracticeFormPage(self.driver)
        practice_form_page.send_form()
        self.assertFalse(practice_form_page.is_form_sended())
        practice_form_page.input_name("Name")
        practice_form_page.input_lastname("LastName")
        selected = practice_form_page.select_gender("Wrong")
        self.assertFalse(selected)
        selected = practice_form_page.select_gender("Male")
        self.assertTrue(selected)
        practice_form_page.input_mobile("wrong")
        practice_form_page.send_form()
        self.assertFalse(practice_form_page.is_form_sended())
        practice_form_page.input_mobile("1111222233")
        practice_form_page.input_email("wrong")
        practice_form_page.send_form()
        self.assertFalse(practice_form_page.is_form_sended())
        practice_form_page.select_date(date(1998, 10, 20))
        selected = practice_form_page.select_hobby("Wrong")
        self.assertFalse(selected)
        selected = practice_form_page.select_hobby("Sports")
        self.assertTrue(selected)
        selected = practice_form_page.select_hobby("Music")
        self.assertTrue(selected)
        practice_form_page.input_email("example@example.com")
        practice_form_page.input_picture("D:\\Trash\\selenium\\test.jpg")
        practice_form_page.input_address("address1010101")
        practice_form_page.input_subject("Wrong")
        self.assertEqual(practice_form_page.subjects_len(), 0)
        time.sleep(5)
        practice_form_page.input_subject("Maths")
        time.sleep(5)
        practice_form_page.input_subject("Arts")
        time.sleep(5)
        self.assertEqual(practice_form_page.subjects_len(), 2)
        practice_form_page.input_state("wrong")
        self.assertFalse(practice_form_page.is_city_enabled())
        practice_form_page.input_state("NCR")
        self.assertTrue(practice_form_page.is_city_enabled())
        practice_form_page.input_city("wrong")
        self.assertTrue(practice_form_page.is_city_empty())
        practice_form_page.input_city("Noida")
        time.sleep(5)
        self.assertFalse(practice_form_page.is_city_empty())
        practice_form_page.send_form()
        self.assertTrue(practice_form_page.is_form_sended())

    def test_demoqa_result(self):
        home_page = page.HomePage(self.driver)
        home_page.click_forms_menu()
        time.sleep(2)
        home_page.click_close_ads()
        home_page.click_practice_form()
        practice_form_page = page.PracticeFormPage(self.driver)
        practice_form_page.input_name("Name")
        practice_form_page.input_lastname("LastName")
        selected = practice_form_page.select_gender("Male")
        self.assertTrue(selected)
        practice_form_page.input_mobile("1111222233")
        practice_form_page.input_email("example@example.com")
        practice_form_page.input_picture("D:\\Trash\\selenium\\test.jpg")
        practice_form_page.input_address("address1010101")
        practice_form_page.select_date(date(1998, 10, 20))
        selected = practice_form_page.select_hobby("Sports")
        self.assertTrue(selected)
        selected = practice_form_page.select_hobby("Music")
        self.assertTrue(selected)
        practice_form_page.input_email("example@example.com")
        practice_form_page.input_picture("D:\\Trash\\selenium\\test.jpg")
        time.sleep(5)
        practice_form_page.input_subject("Maths")
        time.sleep(5)
        practice_form_page.input_subject("Arts")
        time.sleep(5)
        practice_form_page.input_state("NCR")
        practice_form_page.input_city("Noida")
        practice_form_page.send_form()
        time.sleep(5)
        self.assertTrue(practice_form_page.is_form_sended())
        dicts = {
            'Student Name' : 'Name LastName',
            'Student Email' : 'example@example.com',
            'Gender' : 'Male',
            'Mobile' : '1111222233',
            'Date of Birth' : '20 October,1998',
            'Subjects' : 'Maths, Arts',
            'Hobbies' : 'Sports, Music',
            'Picture' : 'test.jpg',
            'Address' : 'address1010101',
            'State and City' : 'NCR Noida'
        }
        for key, value in dicts.items():
            self.assertTrue(practice_form_page.check_row_in_result(key, value))

    def test_demoqa_login(self):
        home_page = page.HomePage(self.driver)
        home_page.click_bookstore_menu()
        bookstore_page = page.BookStorePage(self.driver)
        bookstore_page.click_login_button()
        login_page = page.LoginPage(self.driver)
        login_page.log_in("testuser", "fxSkcKv^6gRxY@sj_bJDXWuqfGN=RnE+")
        self.driver.implicitly_wait(5)
        assert bookstore_page.check_is_logged(), "Not logged!"
        bookstore_page.click_logout_button()

    def test_books_list(self):
        home_page = page.HomePage(self.driver)
        home_page.click_bookstore_menu()
        bookstore_page = page.BookStorePage(self.driver)
        self.driver.implicitly_wait(5)
        self.assertEqual(bookstore_page.get_books_number(),
                         8, "Number of books is not equal 8!")
        self.driver.execute_script('window.scrollBy(0,1000)')
        bookstore_page.change_page_size(5)
        self.driver.implicitly_wait(5)
        self.assertEqual(bookstore_page.get_books_number(),
                         5, "Number of books is not equal 5!")
        bookstore_page.click_next_page_button()
        self.assertEqual(bookstore_page.get_books_number(),
                         3, "Number of books is not equal 3!")
        assert bookstore_page.check_no_next_page(), "There is one more page!"
        bookstore_page.click_prev_page_button()
        self.assertEqual(bookstore_page.get_books_number(),
                         5, "Number of books is not equal 5!")
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
        assert not book_page.is_add_button_on_page(
        ), "Button to add book is on the page!"
        assert book_page.is_login_button_on_page(
        ), "Button to login is not on the page!"
        book_page.click_login()
        self.driver.implicitly_wait(5)
        login_page = page.LoginPage(self.driver)
        login_page.log_in("testuser", "fxSkcKv^6gRxY@sj_bJDXWuqfGN=RnE+")
        self.driver.implicitly_wait(5)
        assert book_page.is_add_button_on_page(
        ), "Button to add book is not on the page!"
        assert not book_page.is_login_button_on_page(
        ), "Button to login is on the page!"
        self.driver.execute_script('window.scrollBy(0,1000)')
        self.driver.implicitly_wait(5)
        result = book_page.add_book()
        self.assertEqual(
            result, "Book added to your collection.", "Book added again!")
        self.driver.implicitly_wait(5)
        result = book_page.add_book()
        self.assertEqual(
            result, "Book already present in the your collection!", "Book added again!")
        self.driver.implicitly_wait(2)
        book_page.click_back()
        self.driver.implicitly_wait(5)
        book_page.click_close_ads()
        self.driver.execute_script('window.scrollBy(0,1000)')
        book_page.click_profile()
        self.driver.implicitly_wait(5)
        profile_page = page.ProfilePage(self.driver)
        self.driver.execute_script('window.scrollBy(0,1000)')
        self.assertTrue(profile_page.is_book_added(
            'Git Pocket Guide'), 'Book is missing!')
        result = profile_page.delete_book_cancel('Git Pocket Guide')
        self.assertEqual(
            result, "Do you want to delete this book?", "Wrong delete message!")
        self.assertTrue(profile_page.is_book_added(
            'Git Pocket Guide'), 'Book is missing!')
        (modal_text, alert_text) = profile_page.delete_book_ok('Git Pocket Guide')
        self.assertEqual(
            modal_text, "Do you want to delete this book?", "Wrong delete message!")
        self.assertEqual(
            alert_text, "Book deleted.", "Wrong alert message!")
        self.driver.implicitly_wait(5)
        self.assertFalse(profile_page.is_book_added(
            'Git Pocket Guide'), 'Book is presented!')
        self.driver.implicitly_wait(5)
        self.driver.execute_script('window.scrollBy(0,-1000)')
        self.assertTrue(profile_page.is_logout_button_on_page(),
                        'Log out button is missing!')
        profile_page.logout()
        self.driver.implicitly_wait(5)
        self.assertEqual(self.driver.current_url,
                         'https://demoqa.com/login', 'Logout fault!')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
