"""
This doesn't work.
"""

from selenium.webdriver.edge import webdriver

from django.test import LiveServerTestCase


class TitleTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver()
        cls.selenium.implicitly_wait(10)
