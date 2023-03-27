import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import textract
# для работы с сохраненными файлами
import os
# в именах сохраненных файлов ставится дата
import datetime
# для очистки папки с сохраненными файлами после теста
import shutil
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions


class PriceTestCase(unittest.TestCase):
    # подготовка к каждому тесту
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        # открытие страницы при начале каждого теста
        self.page = self.driver.get(
            'https://service-online.su/forms/cenniki/'
        )
        # открытие окна авторизации
        elem = self.driver.find_element(By.ID, "enter")
        elem.click()
        time.sleep(2)
        # ввод логина и пароля
        elem = self.driver.find_element(By.NAME, "login")
        elem.send_keys("pasha.desh@yandex.by")
        elem = self.driver.find_element(By.NAME, "password")
        elem.send_keys("jXK9dvbTyCeym5n")
        # нажатие кнопки "Войти"
        elem = self.driver.find_element(By.NAME, "test_enter")
        elem.click()
        # 5 сек ожидания открытия окна
        time.sleep(5)
        # закрытие сообщения об успешном входе
        elem = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label=Close]")
        elem.click()
        time.sleep(2)

    # окончание каждого теста
    def tearDown(self):
        # выход с сайта во избежание блокировки
        # системой защиты от подбора пароля
        ul = self.driver.find_element(By.ID, "menu")
        lis = ul.find_elements(By.TAG_NAME, "li")
        li = lis[-1]
        li.click()
        # закрытие браузера при окончании каждого теста
        self.driver.close()

    # тест на наличие ссылки "Личный кабинет" в меню
    def testAuthorization(self):
        elem = self.driver.find_element(By.ID, "menu")
        self.assertIn("Личный\nкабинет", elem.text)


# тест сохранения одного ценника на английском
    def testOnePrice(self):
        elem = self.driver.find_element(By.ID, "comp_name")
        elem.send_keys("Eurotorg")
        # английский формат даты год/месяц/день
        elem = self.driver.find_element(By.ID, "date")
        elem.clear()
        elem.send_keys("2020/01/13")
        # wait(self.driver, 60).until(
        #     expected_conditions.visibility_of_element_located((By.ID, "a"))
        # )
        print(self.driver.page_source)  
        # выбор белорусского рубля в выпадающем списке валют
        elem = self.driver.find_element(By.NAME, "valyuta")
        elem.click()
        time.sleep(2)
        options = elem.find_elements(By.TAG_NAME, "option")
        for option in options:
            if option.text == "Белорусский рубль":
                option.click()
                break

        elem = self.driver.find_element(By.ID, "tovar_ed_default")
        elem.send_keys("kg")
        elem = self.driver.find_element(By.ID, "tovar_country_default")
        elem.send_keys("RB")

        # таблица с товарами
        elem = self.driver.find_element(By.ID, "tab1")
        tbody = elem.find_element(By.TAG_NAME, "tbody")
        tr = tbody.find_element(By.TAG_NAME, "tr")
        # название товара
        td = tr.find_element(By.CLASS_NAME, "tovar_name")
        field = td.find_element(By.TAG_NAME, "textarea")
        field.send_keys("Candy Southern Night")
        # цена товара - английский формат с точкой
        td = tr.find_element(By.CLASS_NAME, "tovar_cena")
        field = td.find_element(By.TAG_NAME, "input")
        field.send_keys("10.55")

        # жмем ссылку "Скачать"
        elem = self.driver.find_element(By.ID, "download")
        elem.click()
        time.sleep(2)


        # 10 сек ожидания
        # на случай, если Firefox спросит, сохранять файл
        time.sleep(5)

        # проверяем наличие сохраненного файла по названию
        today = datetime.date.today()
        fullpath = (self.savePath +
                "cenniki-new-" +
                today.strftime("%Y-%m-%d") +
                ".pdf"
        )
        self.assertEqual(
            os.path.isfile(fullpath),
            True
        )

        # получаем текст из сохраненного файла
        page = textract.process(fullpath)
        # проверяем наличие введенных значений в тексте файла
        #print(page)
        self.assertIn(b"Eurotorg", page)
        self.assertIn(b"2020/01/13", page)
        self.assertIn(b"kg", page)
        self.assertIn(b"RB", page)
        self.assertIn(b"Candy Southern Night", page)


if __name__ == '__main__':
    unittest.main()
