from selenium.webdriver.common.by import By
from elements import BasePageElement
from locators import BasePageLocators, BookPageLocators, BookStorePageLocators, HomePageLocators, LoginPageLocators, ProfilePageLocators
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class SearchText(BasePageElement):
    # The locator for search box where string is entered
    locator = "searchBox"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def __click_element__(self, by, selector):
        self.driver.find_element(by, selector).click()

    def __input_value__(self, by, selector, value):
        self.driver.find_element(by, selector).send_keys(value)

    def __check_element__(self, by, selector):
        return len(
            self.driver.find_elements(by, selector)) != 0

    def click_profile(self):
        elements = self.driver.find_elements(
            *BasePageLocators.LEFT_MENU_ELEMENTS)
        bookstore = elements[5].find_elements(
            *BasePageLocators.BOOKSTORE_ELEMENTS)
        bookstore[2].click()

    def click_close_ads(self):
        self.__click_element__(*BasePageLocators.CLOSE_ADS_BUTTON)


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
    # Action items for Home Page

    # Variable containing retrieved text

    def click_submit_button(self):
        self.__click_element__(*HomePageLocators.SUBMIT_BUTTON)

    def click_bookstore_menu(self):
        self.__click_element__(*HomePageLocators.BOOKSTORE_MENU)

    def click_elements_menu(self):
        self.__click_element__(*HomePageLocators.ELEMENTS_MENU)

    def click_forms_menu(self):
        self.__click_element__(*HomePageLocators.FORMS_MENU)

    def click_alerts_menu(self):
        self.__click_element__(*HomePageLocators.ALERTS_MENU)

    def click_interactions_menu(self):
        self.__click_element__(*HomePageLocators.INTERACTIONS_MENU)

    def click_widgets_menu(self):
        self.__click_element__(*HomePageLocators.WIDGETS_MENU)


class LoginPage(BasePage):

    def fill_username(self, value):
        self.__input_value__(*LoginPageLocators.USERNAME_INPUT, value)

    def fill_password(self, value):
        self.__input_value__(*LoginPageLocators.PASSWORD_INPUT, value)

    def click_login_button(self):
        self.__click_element__(*LoginPageLocators.LOGIN_BUTTON)


class ResultPage(BasePage):
    # Action items for Result Page

    def check_search_result(self):
        # Checks the result for specified text if found or not
        return "No result forund." not in self.driver.page_source


class BookStorePage(BasePage):

    search_text = SearchText()

    def click_login_button(self):
        self.__click_element__(*BookStorePageLocators.LOGIN_BUTTON)

    def click_logout_button(self):
        self.__click_element__(
            *BookStorePageLocators.LOGOUT_BUTTON)

    def check_books_number(self, number):
        elements = self.driver.find_elements(
            *BookStorePageLocators.ALL_BOOKS_ON_PAGE)
        return len(elements) == number

    def click_book(self, book):
        self.__click_element__(*BookStorePageLocators.book_link(
            book_name=book))

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
        return __check_element__(*BookPageLocators.ADD_BOOK_BUTTON)

    def is_back_button_exist(self):
        return __check_element__(*BookPageLocators.BACK_BUTTON)

    def is_login_button_exist(self):
        return __check_element__(*BookPageLocators.LOGIN_BUTTON)

    def click_add_book(self):
        self.__click_element__(*BookPageLocators.ADD_BOOK_BUTTON)

    def click_back(self):
        self.__click_element__(*BookPageLocators.BACK_BUTTON)

    def click_login(self):
        self.__click_element__(*BookPageLocators.LOGIN_BUTTON)


class ElementsPage(BasePage):
    def is_welcome_page(self):
        return "Please select an item from left to start practice." in self.driver.page_source
