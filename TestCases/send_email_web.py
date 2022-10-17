import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import unittest


class Send_Email(unittest.TestCase):
    def test_send_email(self):
        email, password, receiver_email = "kh928259@gmail.com", "AbC!23456", "khanhhm.94@gmail.com"
        object = "Exercise 1"
        body_content = "My Name is Khanh - I am QA Engineer"

        driver = uc.Chrome(use_subprocess=True)
        url = 'https://gmail.com'
        driver.get(url)
        driver.maximize_window()

        time.sleep(2)
        driver.find_element(By.NAME, 'identifier').send_keys(f'{email}\n')

        time.sleep(10)
        driver.find_element(By.NAME, 'Passwd').send_keys(f'{password}\n')
        #
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".T-I.T-I-KE.L3").click()
        time.sleep(10)

        to_field = driver.find_element(By.CLASS_NAME, 'aFw')
        driver.implicitly_wait(5)
        to_field.send_keys(f'{receiver_email}\n')

        subject_field = driver.find_element(By.NAME, 'subjectbox')
        subject_field.send_keys(f'{object}\n')

        body_field = driver.find_element(By.CSS_SELECTOR, '.Am.Al.editable.LW-avf.tS-tW')
        body_field.send_keys(body_content)

        send_btn = driver.find_element(By.CSS_SELECTOR, '.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3')
        send_btn.click()

        time.sleep(5)