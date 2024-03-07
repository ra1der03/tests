from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import TimeoutException
import unittest

def WaitElement(browser, by=By.TAG_NAME, value=None):
    try:
        return WebDriverWait(browser, 10).until(ec.presence_of_element_located((by, value)))
    except TimeoutException:
        print()


class Test_3(unittest.TestCase):
    def test_3(self):
        expected = 'Successfully ends'
        email = ''  # put in your email
        password = '' # put in your password
        path = ChromeDriverManager().install()
        browser_service = Service(executable_path=path)
        browser = Chrome(service=browser_service)
        browser.get('https://passport.yandex.ru/auth/')

        element = (WaitElement(browser, By.XPATH, '//*[@id="passp-field-login"]').
                   find_element(By.XPATH, '//*[@id="passp-field-login"]'))
        element.click()
        element.send_keys(email)
        button_element = browser.find_element(By.XPATH, '//*[@id="passp:sign-in"]')
        button_element.click()

        el = WaitElement(browser, By.XPATH, '//*[@id="passp-field-passwd"]').find_element(
            By.XPATH, '//*[@id="passp-field-passwd"]')
        el.click()
        el.send_keys(password)
        button_el = (WaitElement(browser, By.XPATH, '//*[@id="passp:sign-in"]')
                     .find_element(By.XPATH, '//*[@id="passp:sign-in"]'))
        button_el.click()
        if WaitElement(browser, By.XPATH, '//*[@id="__next"]/div/header/a').find_element(By.XPATH,
                                                                                         '//*[@id="__next"]/div/header/a'):
            actual = 'Successfully ends'
        else:
            actual = ''
        self.assertEqual(expected, actual)




