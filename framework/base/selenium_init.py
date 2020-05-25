# -*- coding: utf-8 -*-
# @Time    : 2020-05-23
# @Author  : 爱吃苹果的鱼

from selenium import webdriver
import sys, os


class SeleniumInit:
    driver_path = 'C:/Users/Administrator/PycharmProjects/pyTestAutomation/framework/driver/chromedriver.exe'

    def setup(self, browser_type='web'):
        if browser_type == 'web':
            return webdriver.Chrome(executable_path=self.driver_path)
        elif browser_type == 'h5':
            emulation = {'deviceName': 'iPhone 5'}
            options = webdriver.ChromeOptions()
            options.add_experimental_option('mobileEmulation', emulation)
            return webdriver.Chrome(executable_path=self.driver_path, options=options)
        elif browser_type == 'headless':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            return webdriver.Chrome(executable_path=self.driver_path, options=chrome_options)
        else:
            return '类型不是web/h5，请确认参数是否有误'
