from selenium.webdriver.common.by import By
from elements import BasePageElement
from locators import BasePageLocators, BookPageLocators, BookStorePageLocators, HomePageLocators, LoginPageLocators, ProfilePageLocators
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class SearchText(BasePageElement):
    #The locator for search box where string is entered
    locator = "searchBox"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def click_profile(self):
        elements = self.driver.find_elements(
            *BasePageLocators.LEFT_MENU_ELEMENTS)
        bookstore = elements[5].find_elements(
            *BasePageLocators.BOOKSTORE_ELEMENTS)
        bookstore[2].click()

    def click_close_ads(self):
        element = self.driver.find_element(*BasePageLocators.CLOSE_ADS_BUTTON)
        element.click()


class ProfilePage(BasePage):
    def check_books_number(self, number):
        elements = self.driver.find_elements(
            *ProfilePageLocators.ALL_BOOKS_ON_PAGE)
        return len(elements) == number

    def is_book_added(self, book):
        return len(
            self.driver.find_elements(*ProfilePageLocators.book_link(
                book_name=book))) != 0


class HomePage(BasePage):
    #Action items for Home Page

    #Variable containing retrieved text

    def click_submit_button(self):
        #Search is initialized
        element = self.driver.find_element(*HomePageLocators.SUBMIT_BUTTON)
        element.click()

    def click_bookstore_menu(self):
        #Search is initialized
        element = self.driver.find_element(*HomePageLocators.BOOKSHELF_MENU)
        element.click()


class LoginPage(BasePage):
    def fill_username(self, value):
        element = self.driver.find_element(*LoginPageLocators.USERNAME_INPUT)
        element.send_keys(value)

    def fill_password(self, value):
        element = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        element.send_keys(value)

    def click_login_button(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        element.click()


class ResultPage(BasePage):
    #Action items for Result Page

    def check_search_result(self):
        #Checks the result for specified text if found or not
        return "No result forund." not in self.driver.page_source


class BookStorePage(BasePage):

    search_text = SearchText()

    def click_login_button(self):
        element = self.driver.find_element(*BookStorePageLocators.LOGIN_BUTTON)
        element.click()

    def click_logout_button(self):
        element = self.driver.find_element(
            *BookStorePageLocators.LOGOUT_BUTTON)
        element.click()

    def check_books_number(self, number):
        elements = self.driver.find_elements(
            *BookStorePageLocators.ALL_BOOKS_ON_PAGE)
        return len(elements) == number

    def click_book(self, book):
        element = self.driver.find_element(*BookStorePageLocators.book_link(
            book_name=book))
        element.click()

    def change_page_size(self, value):
        element = self.driver.find_element(
            *BookStorePageLocators.SELECT_WRAPPER)
        select_element = element.find_element(
            *BookStorePageLocators.PAGE_SIZE_SELECT)
        select_object = Select(select_element)
        select_object.select_by_value(str(value))

    def click_next_page_button(self):
        element = self.driver.find_element(
            *BookStorePageLocators.NEXT_PAGE_BUTTON_WRAPPER)
        button = element.find_element(By.TAG_NAME, 'button')
        button.click()

    def click_prev_page_button(self):
        element = self.driver.find_element(
            *BookStorePageLocators.PREV_PAGE_BUTTON_WRAPPER)
        button = element.find_element(By.TAG_NAME, 'button')
        button.click()

    def check_no_next_page(self):
        element = self.driver.find_element(
            *BookStorePageLocators.NEXT_PAGE_BUTTON_WRAPPER)
        return len(element.find_elements(By.XPATH, './button[@disabled]')) != 0

    def check_no_prev_page(self):
        element = self.driver.find_element(
            *BookStorePageLocators.PREV_PAGE_BUTTON_WRAPPER)
        return len(element.find_elements(By.XPATH, './button[@disabled]')) != 0

    def check_is_logged(self):
        return "testuser" not in self.driver.page_source


class BookPage(BasePage):
    def is_add_button_exist(self):
        return len(
            self.driver.find_elements(*BookPageLocators.ADD_BOOK_BUTTON)) != 0

    def is_back_button_exist(self):
        return len(
            self.driver.find_elements(*BookPageLocators.BACK_BUTTON)) != 0

    def is_login_button_exist(self):
        return len(
            self.driver.find_elements(*BookPageLocators.LOGIN_BUTTON)) != 0

    def click_add_book(self):
        element = self.driver.find_element(*BookPageLocators.ADD_BOOK_BUTTON)
        element.click()

    def click_back(self):
        element = self.driver.find_element(*BookPageLocators.BACK_BUTTON)
        element.click()

    def click_login(self):
        element = self.driver.find_element(*BookPageLocators.LOGIN_BUTTON)
        element.click()