from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LEFT_MENU_ELEMENTS = (By.CSS_SELECTOR,
                          'div.left-pannel>div.accordion>div.element-group')
    BOOKSTORE_ELEMENTS = (By.CSS_SELECTOR, 'div.element-list>ul.menu-list>li')
    CLOSE_ADS_BUTTON = (By.ID, 'close-fixedban')


class HomePageLocators(object):
    SUBMIT_BUTTON = (By.CLASS_NAME, 'search__submit')
    ELEMENTS_MENU = (By.XPATH, "//*[@class='card mt-4 top-card'][1]")
    FORMS_MENU = (By.XPATH, "//*[@class='card mt-4 top-card'][2]")
    ALERTS_MENU = (By.XPATH, "//*[@class='card mt-4 top-card'][3]")
    WIDGETS_MENU = (By.XPATH, "//*[@class='card mt-4 top-card'][4]")
    INTERACTIONS_MENU = (By.XPATH, "//*[@class='card mt-4 top-card'][5]")
    BOOKSTORE_MENU = (By.XPATH, "//*[@class='card mt-4 top-card'][6]")


class LoginPageLocators(object):
    USERNAME_INPUT = (By.ID, 'userName')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login')


class BookStorePageLocators(object):
    LOGOUT_BUTTON = (By.ID, 'submit')
    LOGIN_BUTTON = (By.ID, 'login')
    BOOK_ROW = (By.CLASS_NAME, 'rt-tr-group')
    ALL_BOOKS_ON_PAGE = (By.CSS_SELECTOR, '.rt-tbody > .rt-tr-group > div a')
    PAGE_SIZE_SELECT = (By.TAG_NAME, 'select')
    SELECT_WRAPPER = (By.CLASS_NAME, 'select-wrap')
    PREV_PAGE_BUTTON_WRAPPER = (By.CLASS_NAME, '-previous')
    NEXT_PAGE_BUTTON_WRAPPER = (By.CLASS_NAME, '-next')

    def book_link(book_name):
        return (By.XPATH, f'//*[@id="see-book-{book_name}"]/a')


class BookPageLocators(object):
    ADD_BOOK_BUTTON = (By.XPATH, "//*[@class='text-right fullButton']/button")
    BACK_BUTTON = (By.CSS_SELECTOR,
                   '.text-left.fullButton>button#addNewRecordButton')
    LOGIN_BUTTON = (By.ID, 'login')


class ProfilePageLocators(object):
    LOGIN_BUTTON = (By.ID, 'login')
    LOGOUT_BUTTON_NEI = (By.ID, 'userName-value')
    ALL_BOOKS_ON_PAGE = (By.CSS_SELECTOR, '.rt-tbody > .rt-tr-group > div a')
    DELETE_BUTTON = (By.XPATH, "//*[@id='delete-record-undefined']")

    MODAL_OK_BUTTON = (By.ID, 'closeSmallModal-ok')
    MODAL_CANCEL_BUTTON = (By.ID, 'closeSmallModal-cancel')
    MODAL_DIALOG = (By.CLASS_NAME, 'modal-dialog')
    MODAL_TEXT = (By.CLASS_NAME, 'modal-body')

    def book_link(book_name):
        return (By.XPATH, f'//*[@id="see-book-{book_name}"]/a')

    def book_delete_link(book_name):
        return (By.XPATH, f".//*[@id='see-book-{book_name}']/../../..//*[@id='delete-record-undefined']")
