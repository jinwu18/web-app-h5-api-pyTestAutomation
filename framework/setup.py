__author__ = 'panyongjun'
from appium import webdriver


class AppSetupClass:
    def __init__(self, os_version, os_name, device_name, app_package, app_activity, appium_port):
        self.os_version = os_version
        self.os_name = os_name
        self.device_name = device_name
        self.app_package = app_package
        self.app_activity = app_activity
        self.appium_port = appium_port

    def setup(self):
        capabilities = {"platformVersion": self.os_version,
                        "platformName": self.os_name,
                        "deviceName": self.device_name,
                        "appPackage": self.app_package,
                        "appActivity": self.app_activity,
                        "autoLaunch": True,
                        "autoGrantPermissions": True,
                        "newCommandTimeout": 120,
                        "deviceReadyTimeout": 120,
                        "noReset": True,
                        }
        driver = webdriver.Remote("http://127.0.0.1:" + self.appium_port + "/wd/hub", capabilities)
        return driver
