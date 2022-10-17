import unittest
from configs import appium_driver

"""
This class is responsible for creating driver connection with appium server
"""


class BaseSpecification(unittest.TestCase):
    def setUp(self):
        self.driver = appium_driver.Driver().get_driver()

    def tearDown(self):
        self.driver.quit()