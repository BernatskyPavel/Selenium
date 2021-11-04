from selenium.webdriver.common.by import By
from locators import BasePageLocators, BookPageLocators, BookStorePageLocators, HomePageLocators, LoginPageLocators, ProfilePageLocators
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support.relative_locator import locate_with


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def __click_element__(self, by, selector):
        self.driver.find_element(by, selector).click()

    def __input_value__(self, by, selector, value):
        self.driver.find_element(by, selector).send_keys(value)

    def __check_element__(self, by, selector):
        return self.__get_elements_number__(by, selector) != 0

    def __get_elements_number__(self, by, selector):
        return len(self.driver.find_elements(by, selector))

    def click_profile(self):
        elements = self.driver.find_elements(
            *BasePageLocators.LEFT_MENU_ELEMENTS)
        bookstore = elements[5].find_elements(
            *BasePageLocators.BOOKSTORE_ELEMENTS)
        bookstore[2].click()

    def click_close_ads(self):
        self.__click_element__(*BasePageLocators.CLOSE_ADS_BUTTON)


class ProfilePage(BasePage):
    def get_books_number(self):
        return self.__get_elements_number__(*ProfilePageLocators.ALL_BOOKS_ON_PAGE)

    def is_book_added(self, book):
        return self.__check_element__(*ProfilePageLocators.book_link(book))

    def __delete_book__(self, book_name):
        self.__click_element__(
            *ProfilePageLocators.book_delete_link(book_name))

    def delete_book_ok(self, book_name):
        self.__delete_book__(book_name)
        modal = wait(self.driver,
                     10).until(expected_conditions.visibility_of_element_located((ProfilePageLocators.MODAL_DIALOG)))
        text = modal.find_element(*ProfilePageLocators.MODAL_TEXT).text
        modal.find_element(*ProfilePageLocators.MODAL_OK_BUTTON).click()

        alert = wait(self.driver,
                     10).until(expected_conditions.alert_is_present())
        atext = alert.text
        alert.accept()
        return (text, atext)

    def delete_book_cancel(self, book_name):
        self.__delete_book__(book_name)
        modal = wait(self.driver,
                     10).until(expected_conditions.visibility_of_element_located((ProfilePageLocators.MODAL_DIALOG)))
        text = modal.find_element(*ProfilePageLocators.MODAL_TEXT).text
        modal.find_element(*ProfilePageLocators.MODAL_CANCEL_BUTTON).click()
        return text

    def is_logout_button_on_page(self):
        nei = self.driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON_NEI)
        return len(self.driver.find_elements(locate_with(By.TAG_NAME, "button").to_right_of(nei))) != 0

    def logout(self):
        nei = self.driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON_NEI)
        self.driver.find_element(locate_with(
            By.TAG_NAME, "button").to_right_of(nei)).click()


class HomePage(BasePage):
    # Action items for Home Page
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
    def log_in(self, username, password):
        self.__input_value__(*LoginPageLocators.USERNAME_INPUT, username)
        self.__input_value__(*LoginPageLocators.PASSWORD_INPUT, password)
        self.__click_element__(*LoginPageLocators.LOGIN_BUTTON)


class BookStorePage(BasePage):

    def click_login_button(self):
        self.__click_element__(*BookStorePageLocators.LOGIN_BUTTON)

    def click_logout_button(self):
        self.__click_element__(
            *BookStorePageLocators.LOGOUT_BUTTON)

    def get_books_number(self):
        return self.__get_elements_number__(*BookStorePageLocators.ALL_BOOKS_ON_PAGE)

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

    def is_add_button_on_page(self):
        return self.__check_element__(*BookPageLocators.ADD_BOOK_BUTTON)

    def is_back_button_on_page(self):
        return self.__check_element__(*BookPageLocators.BACK_BUTTON)

    def is_login_button_on_page(self):
        return self.__check_element__(*BookPageLocators.LOGIN_BUTTON)

    def add_book(self):
        self.__click_element__(*BookPageLocators.ADD_BOOK_BUTTON)
        alert = wait(self.driver,
                     10).until(expected_conditions.alert_is_present())
        text = alert.text
        alert.accept()
        return text

    def click_back(self):
        self.__click_element__(*BookPageLocators.BACK_BUTTON)

    def click_login(self):
        self.__click_element__(*BookPageLocators.LOGIN_BUTTON)


class ElementsPage(BasePage):
    def is_welcome_page(self):
        return "Please select an item from left to start practice." in self.driver.page_source
