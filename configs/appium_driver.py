from appium.options.android import UiAutomator2Options
from appium import webdriver


class Driver:
    def __init__(self):
        self.instance = None

    def get_driver(self):
        options = UiAutomator2Options().load_capabilities({
            "app": "bs://0cd639d5c8fe056bca0c09ce50fb3e0a84e2de16",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            'bstack:options': {
                "userName": "kennit1",
                "accessKey": "XksytfRhwFFesCaU6CeG"
            }
        })

        self.instance = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
        return self.instance
