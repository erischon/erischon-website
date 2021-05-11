from django.test import LiveServerTestCase
from selenium import webdriver
import unittest
import os
from unittest import skipIf



class BlogTest(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def tearDown(self):
        self.driver.quit()

    @skipIf(os.getenv('DJANGO_SETTINGS_MODULE') == 'core.settings.travis', 'Travis')
    def test_blog_hp(self):
        """ Testing opening HP blog page. """
        self.driver.get('http://localhost:8000/blog')

        self.assertIn("Eri Schön - Le Blog", self.driver.title)
