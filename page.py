from selenium.webdriver.common.by import By
from locators import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.keys import Keys
from enum import Enum

class BasePage(object):
    
    class Menus(Enum):
        ELEMENTS = 0
        FORMS = 1
        ALERTS = 2
        WIDGETS = 3
        INTERACTIONS = 4
        BOOKSTORE = 5

    class Elements(Enum):
        TEXT_BOX = 0
        CHECK_BOX = 1
        RADIO_BTN = 2
        WEB_TABLES = 3
        BTNS = 4
        LINKS = 5
        BROKEN_LINKS = 6
        UPLOADS = 7
        DYNAMIC = 8
    class Forms(Enum):
        PRACTICE = 0
    class ALERTS(Enum):
        BROWSER = 0
        ALERTS = 1
        FRAMES = 2
        NESTED_FRAMES = 3
        MODAL = 4
    class WIDGETS(Enum):
        ACCORDIAN = 0
        AUTO_COMPLETE = 1
        DATE = 2
        SLIDER = 3
        PROGRESS_BAR = 4
        TABS = 5
        TOOL_TIPS = 6
        MENU = 7
        SELECT_MENU =8
    class INTERACTIONS(Enum):
        SORTABLE = 0
        SELECTABLE = 1
        RESIZABLE = 2
        DROPPABLE = 3
        DRAGABBLE = 4
    class BOOK_STORE(Enum):
        LOGIN = 0
        BOOK_STORE = 1
        PROFILE = 2
        BOOK_STORE_API = 3
    
    def __init__(self, driver):
        self.driver = driver

    def __click_element__(self, by, selector):
        self.driver.find_element(by, selector).click()

    def __input_value__(self, by, selector, value):
        self.driver.find_element(by, selector).send_keys(value)

    def __clear_value__(self, by, selector):
        self.driver.find_element(by, selector).clear()

    def __get_element_value__(self, by, selector):
        #self.driver.find_element(by, selector).text
        return self.driver.find_element(by, selector).get_attribute("innerText")

    def __check_element__(self, by, selector):
        return self.__get_elements_number__(by, selector) != 0

    def __get_elements_number__(self, by, selector):
        return len(self.driver.find_elements(by, selector))

    def __scroll_to_element__(self, element):
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)

    def __scroll_to__(self,  by, selector):
        element = self.driver.find_element(by, selector)
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)

    def __click_left_menu__(self, menu):
        menu = self.driver.find_elements(
            *BasePageLocators.LEFT_MENU_ELEMENTS)[menu.value]
        self.__scroll_to_element__(menu)
        menu.click()
    
    def __click_left_submenu__(self, menu, submenu):
        if not self.is_menu_opened(menu):
            self.__click_left_menu__(menu)
        menu = self.driver.find_elements(
            *BasePageLocators.LEFT_MENU_ELEMENTS)[menu.value]
        self.__scroll_to_element__(menu)
        submenu = menu.find_elements(
            *BasePageLocators.LEFT_SUBMENU_ELEMENTS)[submenu.value]
        self.__scroll_to_element__(submenu)
        submenu.click()

    def is_menu_opened(self, menu):
        menu = self.driver.find_elements(
            *BasePageLocators.LEFT_MENU_ELEMENTS)[menu.value]
        return len(menu.find_elements(By.CSS_SELECTOR, "div.show")) != 0

    def click_profile(self):
        self.__click_left_submenu__(self.Menus.BOOKSTORE, self.BOOK_STORE.PROFILE)

    def click_practice_form(self):
        self.__click_left_submenu__(self.Menus.FORMS, self.Forms.PRACTICE)

    def click_close_ads(self):
        self.__click_element__(*BasePageLocators.CLOSE_ADS_BUTTON)
        self.driver.refresh()

class PracticeFormPage(BasePage):
    def get_state_value(self):
        return self.__get_element_value__(*FormPageLocators.STATE_INPUT_VALUE)
    
    def input_state(self, state):
        self.__scroll_to__(*FormPageLocators.STATE_INPUT)
        self.__input_value__(*FormPageLocators.STATE_INPUT, state)
        self.__input_value__(*FormPageLocators.STATE_INPUT, Keys.TAB)
        self.__scroll_to__(*FormPageLocators.STATE_INPUT)

    def is_city_enabled(self):
        return self.driver.find_element(*FormPageLocators.CITY_INPUT).get_attribute("disabled") is None

    def get_city_value(self):
        return self.__get_element_value__(*FormPageLocators.CITY_INPUT_VALUE)
    
    def is_city_empty(self):
        return not self.__check_element__(*FormPageLocators.CITY_INPUT_VALUE)

    def input_city(self, state):
        self.__scroll_to__(*FormPageLocators.CITY_INPUT)
        self.__input_value__(*FormPageLocators.CITY_INPUT, state)
        self.__input_value__(*FormPageLocators.CITY_INPUT, Keys.TAB)
        self.__scroll_to__(*FormPageLocators.CITY_INPUT)

    def input_name(self, name):
        self.__scroll_to__(*FormPageLocators.NAME_INPUT)
        self.__input_value__(*FormPageLocators.NAME_INPUT, name)
    
    def input_lastname(self, lastname):
        self.__scroll_to__(*FormPageLocators.LASTNAME_INPUT)
        self.__input_value__(*FormPageLocators.LASTNAME_INPUT, lastname)

    def input_mobile(self, mobile):
        self.__scroll_to__(*FormPageLocators.MOBILE_INPUT)
        self.__clear_value__(*FormPageLocators.MOBILE_INPUT)
        self.__input_value__(*FormPageLocators.MOBILE_INPUT, mobile)

    def select_gender(self, gender):
        self.__scroll_to__(*FormPageLocators.GENDER_INPUTS)
        if not self.__check_element__(*FormPageLocators.gender_option(gender)):
            return False
        self.__click_element__(*FormPageLocators.gender_option(gender))
        return True

    def is_form_sended(self):
        return self.__check_element__(*FormPageLocators.RESULT_DIALOG)

    def send_form(self):
        self.__scroll_to__(*FormPageLocators.SUBMIT_BTN)
        self.__click_element__(*FormPageLocators.SUBMIT_BTN)

    def input_email(self, email):
        self.__scroll_to__(*FormPageLocators.EMAIL_INPUT)
        self.__clear_value__(*FormPageLocators.EMAIL_INPUT)
        self.__input_value__(*FormPageLocators.EMAIL_INPUT, email)
    
    def select_hobby(self, hobby):
        self.__scroll_to__(*FormPageLocators.HOBBIES_INPUTS)
        if not self.__check_element__(*FormPageLocators.hobbies_option(hobby)):
            return False
        self.__click_element__(*FormPageLocators.hobbies_option(hobby))
        return True

    def input_subject(self, subject):
        self.__scroll_to__(*FormPageLocators.SUBJECTS_INPUT)
        self.__clear_value__(*FormPageLocators.SUBJECTS_INPUT)
        self.__input_value__(*FormPageLocators.SUBJECTS_INPUT, subject)
        self.__input_value__(*FormPageLocators.SUBJECTS_INPUT, Keys.TAB)

    def subjects_len(self):
        return self.__get_elements_number__(*FormPageLocators.SUBJECTS_VALUES)

    def input_picture(self, path):
        self.__scroll_to__(*FormPageLocators.PICTURE_INPUT)
        self.__input_value__(*FormPageLocators.PICTURE_INPUT, path)

    def input_address(self, adr):
        self.__scroll_to__(*FormPageLocators.ADDRESS_INPUT)
        self.__input_value__(*FormPageLocators.ADDRESS_INPUT, adr)

    def select_date(self, date):
        self.__scroll_to__(*FormPageLocators.BIRTH_INPUT)
        self.__click_element__(*FormPageLocators.BIRTH_INPUT)
        month = self.driver.find_element(*FormPageLocators.BIRTH_MONTH)
        month.click()
        month.find_element(By.CSS_SELECTOR, f"option[value='{date.month-1}']").click()
        year = self.driver.find_element(*FormPageLocators.BIRTH_YEAR)
        year.click()
        year.find_element(By.CSS_SELECTOR, f"option[value='{date.year}']").click()
        self.__click_element__(*FormPageLocators.birth_day(date.day))

    def check_row_in_result(self, key, value):
        return self.__check_element__(*FormPageLocators.table_row(key, value))    

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
