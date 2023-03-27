import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class Kalkpro(unittest.TestCase):
    # https://kalk.pro/finish/wallpaper/
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()

    def test_about_breadcrumbs(self):
        driver = self.driver
        # открытие в Firefox страницы http://www.python.org
        driver.get("http://www.python.org")
        # получаем список ссылок в меню About по CSS-селектору
        elems = driver.find_elements(By.CSS_SELECTOR, '#about ul li a')
        # перебираем полученные подпункты меню,
        # выписываем названия и ссылки в отдельные списки
        # потому что при переходе по ссылкам на другие страницы
        # связь со списком подпунктов будет потеряна
        href_list = []
        name_list = []
        for e in elems:
            href_list.append(e.get_attribute("href"))
            name_list.append(e.get_attribute('innerHTML'))

        # перебираем полученные ссылки (кроме последней)
        for i in range(len(href_list)):
            # переходим по ссылке
            driver.get(
                href_list[i]
            )
            # получаем строчку хлебных крошек
            elem = driver.find_element(By.CSS_SELECTOR, '.breadcrumbs')
            # проверка наличия в хлебных крошках ссылки на пункт About
            self.assertIn("About", elem.get_attribute('innerHTML'))
            # проверка наличия в хлебных крошках
            # наличия названия текущего пункта
            self.assertIn(
                # название текущего пункта
                name_list[i],
                # строчка хлебных крошек
                elem.get_attribute('innerHTML')
            )
            # ждем 5 секунд
            time.sleep(3)
