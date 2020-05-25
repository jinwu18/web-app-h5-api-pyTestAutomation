# -*- coding: utf-8 -*-
# @Time    : 2020-05-24
# @Author  : 爱吃苹果的鱼

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from logger import logger


class AppCommon:

    def __init__(self, driver):
        self.driver = driver

    def toast_chk(self, toast):
        try:
            WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath('找到了toast"' + toast + '"'))
            logger.info('找到了toast"' + toast + '"')
            return True
        except:
            logger.info('找不到"' + toast + '"')
            return False

    def device_x_get(self):
        return self.driver.get_window_size()['width']

    def device_y_get(self):
        return self.driver.get_window_size()['height']

    def tap_click(self, x, y):
        act = TouchAction(self.driver)
        act.tap(x=x, y=y).perform()

    def swipe_left(self, swipe_times=1):
        logger.info("向左滑动" + str(swipe_times) + "次")
        size = self.driver.get_window_size()
        width = size["width"]
        height = size["height"]
        for i in range(0, swipe_times):
            self.driver.swipe(width*0.8, height*0.5, width*0.2, height*0.5, duration=800)
            # time.sleep(1)

    def swipe_right(self, swipe_times=1):
        logger.info("向右滑动" + str(swipe_times) + "次")
        size = self.driver.get_window_size()
        width = size["width"]
        height = size["height"]
        for i in range(0, swipe_times):
            self.driver.swipe(width*0.2, height*0.5, width*0.8, height*0.5)
            time.sleep(1)

    def swipe_up(self, swipe_times=1):
        logger.info("向上滑动" + str(swipe_times) + "次")
        size = self.driver.get_window_size()
        width = size["width"]
        height = size["height"]
        for i in range(0, swipe_times):
            self.driver.swipe(width*0.5, height*0.8, width*0.5, height*0.2)
            time.sleep(1)

    def swipe_down(self, swipe_times=1):
        logger.info("向下滑动" + str(swipe_times) + "次")
        size = self.driver.get_window_size()
        width = size["width"]
        height = size["height"]
        for i in range(0, swipe_times):
            self.driver.swipe(width*0.5, height*0.2, width*0.5, height*0.8)
            time.sleep(1)
