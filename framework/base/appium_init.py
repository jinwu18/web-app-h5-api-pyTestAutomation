# -*- coding: utf-8 -*-
# @Time    : 2020-05-23
# @Author  : 爱吃苹果的鱼

from appium import webdriver


class AppiumInit:

    def __init__(self, platformVersion, platformName, deviceName, appPackage, appActivity, appiumPort):
        self.platformVersion = platformVersion
        self.platformName = platformName
        self.deviceName = deviceName
        self.appPackage = appPackage
        self.appActivity = appActivity
        self.appiumPort = appiumPort

    def setup(self):
        capabilities = {"platformVersion": self.platformVersion,
                        "platformName": self.platformName,
                        "deviceName": self.deviceName,
                        "appPackage": self.appPackage,
                        "appActivity": self.appActivity,
                        "autoLaunch": True,
                        "autoGrantPermissions": True,
                        "newCommandTimeout": 120,
                        "deviceReadyTimeout": 120,
                        "noReset": True,
                        }
        return webdriver.Remote("http://127.0.0.1:" + self.appiumPort + "/wd/hub", capabilities)
