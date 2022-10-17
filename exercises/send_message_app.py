import time
from appium.webdriver.common.appiumby import AppiumBy
from configs.base_specification import BaseSpecification


class SendMessage(BaseSpecification):
    def test_send_Message(self):
        time.sleep(2)
        textbox_email = self.driver.find_element(AppiumBy.ID, 'loginEmailEdit')
        textbox_email.send_keys("khanhhm.94@gmail.com")

        textbox_password = self.driver.find_element(AppiumBy.ID, 'loginPasswordEdit')
        textbox_password.send_keys("Abc123456")

        btn_signin = self.driver.find_element(AppiumBy.ID, 'loginSignInBut')
        btn_signin.click()

        time.sleep(3)
        item = self.driver.find_element(AppiumBy.ID, 'itemContactListEmailView')
        item.click()

        chat = self.driver.find_element(AppiumBy.ID, 'context_chat')
        chat.click()

        chat_edit_text = self.driver.find_element(AppiumBy.ID, 'chatEditText')
        chat_edit_text.send_keys("Hello Friend")

        chat_send_button = self.driver.find_element(AppiumBy.ID, 'chatSendBut')
        chat_send_button.click()

        list_of_chat = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.vsee.vsee.beta:id/message_text']")
        print(len(list_of_chat))
        expect_messages = []

        for value in list_of_chat:
            msg = value.get_attribute("text")
            print(msg)
            expect_messages.append(msg)

        print(expect_messages)
