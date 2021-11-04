from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class BasePageElement(object):
    # Used in every page
    def __set__(self, obj, value):
        # Contains specified text
        driver = obj.driver
        WebDriverWait(
            driver,
            100).until(lambda driver: driver.find_element(By.ID, self.locator))
        element = driver.find_element(By.ID, self.locator)
        element.clear()
        element.send_keys(value)

    def __get__(self, obj, owner):
        '''Gets the text of specified object'''
        driver = obj.driver
        WebDriverWait(
            driver,
            100).until(lambda driver: driver.find_element(By.ID, self.locator))
        element = driver.find_element(By.ID, self.locator)
        return element.get_attribute("value")
