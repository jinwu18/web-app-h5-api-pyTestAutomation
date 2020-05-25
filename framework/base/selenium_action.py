# -*- coding: utf-8 -*-
# @Time    : 2020-05-23
# @Author  : 爱吃苹果的鱼

import time
from logger import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


class SeleniumActionAPI:
    def __init__(self, driver):
        self.driver = driver

    def to_url(self, url):
        self.driver.get(url)

    def iframe_switch_to_default(self):
        self.driver.driver.switch_to.default_content()

    def iframe_switch(self, iframe_id_or_name):
        self.driver.switch_to.frame(iframe_id_or_name)

    def ele_list_get_by_id(self, ele_id):
        return self.driver.find_elements_by_id(ele_id)

    def ele_list_get_by_name(self, name):
        return self.driver.find_elements_by_name(name)

    def ele_list_get_by_xpath(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    def ele_list_get_by_css_selector(self, css_selector):
        return self.driver.find_elements_by_css_selector(css_selector)

    def ele_list_get_by_class_name(self, class_name):
        return self.driver.find_elements_by_class_name(class_name)

    def ele_list_get_by_link_text(self, link_text):
        return self.driver.find_elements_by_link_text(link_text)

    def ele_list_get_by_partial_link_text(self, partial_link_text):
        return self.driver.find_elements_by_partial_link_text(partial_link_text)

    def ele_list_get_by_accessibility_id(self, accessibility_id):
        return self.driver.find_elements_by_accessibility_id(accessibility_id)

    def ele_list_get_by__android_uiautomator(self, uia_string):
        return self.driver.find_elements_by_android_uiautomator(uia_string)

    def ele_list_get_by_andriod_viewtag(self, viewtag):
        return self.driver.find_elements_by_android_viewtag(viewtag)

    def ele_list_get_by_custom(self, selector):
        return self.driver.find_elements_by_custom(selector)

    def ele_list_get_by_tag_name(self, tag_name):
        return self.driver.find_elements_by_tag_name(tag_name)

    def ele_display_chk(self, locator):
        WebDriverWait(self.driver, 5, 0.5).until(ec.presence_of_element_located(locator))

    def ele_get_by_id(self, ele_id):
        return self.driver.find_element_by_id(ele_id)

    def ele_get_by_name(self, name):
        return self.driver.find_element_by_name(name)

    def ele_get_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def ele_get_by_css_selector(self, css_selector):
        return self.driver.find_element_by_css_selector(css_selector)

    def ele_get_by_class_name(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    def ele_get_by_link_text(self, link_text):
        return self.driver.find_element_by_link_text(link_text)

    def ele_get_by_partial_link_text(self, partial_link_text):
        return self.driver.find_element_by_partial_link_text(partial_link_text)

    def ele_get_by_accessibility_id(self, accessibility_id):
        return self.driver.find_element_by_accessibility_id(accessibility_id)

    def ele_get_by__android_uiautomator(self, uia_string):
        return self.driver.find_element_by_android_uiautomator(uia_string)

    def ele_get_by_andriod_viewtag(self, viewtag):
        return self.driver.find_element_by_android_viewtag(viewtag)

    def ele_get_by_custom(self, selector):
        return self.driver.find_element_by_custom(selector)

    def ele_get_by_tag_name(self, tag_name):
        return self.driver.find_element_by_tag_name(tag_name)

    def ele_click_by_id(self, ele_id):
        ele_text = self.driver.find_element_by_id(ele_id).text
        self.driver.find_element_by_id(ele_id).click()
        logger.info("点击'" + ele_text + "'")

    def ele_click_by_name(self, name):
        ele_text = self.driver.find_element_by_name(name).text
        self.driver.find_element_by_name(name).click()
        logger.info("点击'" + ele_text + "'")

    def ele_click_by_xpath(self, xpath):
        ele_text = self.driver.find_element_by_xpath(xpath).text
        self.driver.find_element_by_xpath(xpath).click()
        logger.info("点击'" + ele_text + "'")

    def ele_click_by_css_selector(self, css_selector):
        ele_text = self.driver.find_element_by_css_selector(css_selector).text
        self.driver.find_element_by_css_selector(css_selector).click()
        logger.info("点击'" + ele_text + "'")

    def ele_click_by_class_name(self, class_name):
        ele_text = self.driver.find_element_by_class_name(class_name).text
        self.driver.find_element_by_class_name(class_name).click()
        logger.info("点击'" + ele_text + "'")

    def ele_click_by_link_text(self, link_text):
        ele_text = self.driver.find_element_by_link_text(link_text).text
        self.driver.find_element_by_link_text(link_text).click()
        logger.info("点击'" + ele_text + "'")

    def ele_click_by_partial_link_text(self, partial_link_text):
        ele_text = self.driver.find_element_by_partial_link_text(partial_link_text).text
        self.driver.find_element_by_partial_link_text(partial_link_text).click()
        logger.info("点击'" + ele_text + "'")

    def ele_click_by_accessibility_id(self, accessibility_id):
        ele_text = self.driver.find_element_by_accessibility_id(accessibility_id).text
        self.driver.find_element_by_accessibility_id(accessibility_id).click()
        logger.info("点击'" + ele_text + "'")

    def ele_click_by__android_uiautomator(self, uia_string):
        ele_text = self.driver.find_element_by_android_uiautomator(uia_string).text
        self.driver.find_element_by_android_uiautomator(uia_string).click()
        logger.info("点击'" + ele_text + "'")

    def ele_click_by_andriod_viewtag(self, viewtag):
        ele_text = self.driver.find_element_by_android_viewtag(viewtag).text
        self.driver.find_element_by_android_viewtag(viewtag).click()
        logger.info("点击'" + ele_text + "'")

    def ele_click_by_custom(self, selector):
        ele_text = self.driver.find_element_by_custom(selector).text
        self.driver.find_element_by_custom(selector).click()
        logger.info("点击'" + ele_text + "'")

    def ele_click_by_tag_name(self, tag_name):
        ele_text = self.driver.find_elements_by_tag_name(tag_name).text
        self.driver.find_elements_by_tag_name(tag_name).click()
        logger.info("点击'" + ele_text + "'")

    def alert_text_get(self):
        logger.info("Alert text='" + self.driver.switch_to_alert().text + "'")
        return self.driver.switch_to_alert().text

    def alert_accept(self):
        logger.info("Accept alert")
        self.driver.switch_to_alert().accept()

    def alert_dismiss(self):
        logger.info("Dismiss alert")
        self.driver.switch_to_alert().dismiss()

    @staticmethod
    def ele_press_enter(ele):
        logger.info("点击回车按钮")
        ele.send_keys(Keys.ENTER)

    @staticmethod
    def ele_send_keys(ele, text):
        logger.info("文本框传值'" + text + "'")
        ele.send_keys(text)

    @staticmethod
    def ele_clear(ele):
        logger.info("清空文本框")
        ele.clear()
