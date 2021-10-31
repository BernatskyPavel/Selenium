from selenium.webdriver.common.by import By


class HomePageLocators(object):
    #Should contain all locators from main page
    SUBMIT_BUTTON = (By.CLASS_NAME, 'search__submit')
    BOOKSHELF_MENU = (By.XPATH, "//*[@class='card mt-4 top-card'][6]")


class BookStorePageLocators(object):
    #Should contain all locators from main page
    LOGOUT_BUTTON = (By.ID, 'submit')
    USERNAME_INPUT = (By.ID, 'userName')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login')
    BOOK_ROW = (By.CLASS_NAME, 'rt-tr-group')
    ALL_BOOKS_ON_PAGE = (By.CSS_SELECTOR, '.rt-tbody > .rt-tr-group > div a')
    PAGE_SIZE_SELECT = (By.TAG_NAME, 'select')
    SELECT_WRAPPER = (By.CLASS_NAME, 'select-wrap')
    PREV_PAGE_BUTTON_WRAPPER = (By.CLASS_NAME, '-previous')
    NEXT_PAGE_BUTTON_WRAPPER = (By.CLASS_NAME, '-next')

    def book_link(self, book):
        return (By.XPATH, '//*[@id="see-book-Git ' + book + '"]/a')

    #//*[@id="see-book-Git Pocket Guide"]/a
    #//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]


class BookPageLocators(object):
    ADD_BOOK_BUTTON = (By.ID, 'addNewRecordButton')
    BACK_BUTTON = (By.ID, 'addNewRecordButton')


class ResultPageLocators(object):
    #It should contain locators from result page
    pass