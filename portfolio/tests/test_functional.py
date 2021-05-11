import unittest
import os

from django.test import LiveServerTestCase
from selenium import webdriver
from unittest import skipIf


class BlogTest(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def tearDown(self):
        self.driver.quit()

    @skipIf(os.getenv('DJANGO_SETTINGS_MODULE') == 'core.settings.travis', 'Travis')
    def test_blog_hp(self):
        """ Testing opening HP blog page. """
        self.driver.get('http://localhost:8000/portfolio')

        self.assertIn("Eri Schön - Portfolio", self.driver.title)
