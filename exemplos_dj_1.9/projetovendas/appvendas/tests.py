from django.test import TestCase

# Create your tests here.

import datetime

from django.utils import timezone
from django.test import TestCase
import time


from selenium import webdriver




class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        import selenium.webdriver.chrome.service as service

        i = '/Users/valerio/Downloads/imagem.png'
        c = '/Users/valerio/Downloads/chromedriver'
        g = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
        service = service.Service(c)
        service.start()
        capabilities = {'chrome.binary': g}
        driver = webdriver.Remote(service.service_url, capabilities)
        driver.get('http://localhost:8000/appvendas/');
        time.sleep(3)  # Let the user actually see something!
        driver.get('http://localhost:8000/appvendas/produtos');
        time.sleep(3)  # Let the user actually see something!
        driver.get('http://localhost:8000/appvendas/clientes');
        time.sleep(3)  # Let the user actually see something!
        """

        driver.get('http://www.google.com/xhtml');
        time.sleep(3)  # Let the user actually see something!

        search_box = driver.find_element_by_name('q')
        search_box.send_keys('Valerio Gutemberg ')
        driver.get_screenshot_as_file(i)
        search_box.submit()
        time.sleep(10)  # Let the user actually see something!
        """
        driver.quit()
