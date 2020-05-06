__author__ = 'panyongjun'

import time
from logger import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def ele_list_get_by_id(driver,  id):
        return driver.find_elements_by_id(id)


def ele_list_get_by_name(driver, name):
    return driver.find_elements_by_name(name)


def ele_list_get_by_xpath(driver, xpath):
    return driver.find_elements_by_xpath(xpath)


def ele_list_get_by_css_selector(driver, css_selector):
    return driver.find_elements_by_css_selector(css_selector)


def ele_list_get_by_class_name(driver, class_name):
    return driver.find_elements_by_class_name(class_name)


def ele_list_get_by_link_text(driver, link_text):
    return driver.find_elements_by_link_text(link_text)


def ele_list_get_by_partial_link_text(driver, partial_link_text):
    return driver.find_elements_by_partial_link_text(partial_link_text)


def ele_list_get_by_accessibility_id(driver, accessibility_id):
    return driver.find_elements_by_accessibility_id(accessibility_id)


def ele_list_get_by__android_uiautomator(driver, uia_string):
    return driver.find_elements_by_android_uiautomator(uia_string)


def ele_list_get_by_andriod_viewtag(driver, viewtag):
    return driver.find_elements_by_android_viewtag(viewtag)


def ele_list_get_by_custom(driver, selector):
    return driver.find_elements_by_custom(selector)


def ele_list_get_by_tag_name(driver, tag_name):
    return driver.find_elements_by_tag_name(tag_name)


def ele_display_chk(driver, locator):
    WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(locator))


def ele_get_by_id(driver, id):
    return driver.find_element_by_id(id)


def ele_get_by_name(driver, name):
    return driver.find_element_by_name(name)


def ele_get_by_xpath(driver, xpath):
    return driver.find_element_by_xpath(xpath)


def ele_get_by_css_selector(driver, css_selector):
    return driver.find_element_by_css_selector(css_selector)


def ele_get_by_class_name(driver, class_name):
    return driver.find_element_by_class_name(class_name)


def ele_get_by_link_text(driver, link_text):
    return driver.find_element_by_link_text(link_text)


def ele_get_by_partial_link_text(driver, partial_link_text):
    return driver.find_element_by_partial_link_text(partial_link_text)


def ele_get_by_accessibility_id(driver, accessibility_id):
    return driver.find_element_by_accessibility_id(accessibility_id)


def ele_get_by__android_uiautomator(driver, uia_string):
    return driver.find_element_by_android_uiautomator(uia_string)


def ele_get_by_andriod_viewtag(driver, viewtag):
    return driver.find_element_by_android_viewtag(viewtag)


def ele_get_by_custom(driver, selector):
    return driver.find_element_by_custom(selector)


def ele_get_by_tag_name(driver, tag_name):
    return driver.find_element_by_tag_name(tag_name)


def ele_click_by_id(driver, id):
    ele_text = driver.find_element_by_id(id).text
    driver.find_element_by_id(id).click()
    logger.info("点击'" + ele_text + "'")


def ele_click_by_name(driver, name):
    ele_text = driver.find_element_by_name(name).text
    driver.find_element_by_name(name).click()
    logger.info("点击'" + ele_text + "'")


def ele_click_by_xpath(driver, xpath):
    ele_text = driver.find_element_by_xpath(xpath).text
    driver.find_element_by_xpath(xpath).click()
    logger.info("点击'" + ele_text + "'")


def ele_click_by_css_selector(driver, css_selector):
    ele_text = driver.find_element_by_css_selector(css_selector).text
    driver.find_element_by_css_selector(css_selector).click()
    logger.info("点击'" + ele_text + "'")


def ele_click_by_class_name(driver, class_name):
    ele_text = driver.find_element_by_class_name(class_name).text
    driver.find_element_by_class_name(class_name).click()
    logger.info("点击'" + ele_text + "'")


def ele_click_by_link_text(driver, link_text):
    ele_text = driver.find_element_by_link_text(link_text).text
    driver.find_element_by_link_text(link_text).click()
    logger.info("点击'" + ele_text + "'")


def ele_click_by_partial_link_text(driver, partial_link_text):
    ele_text = driver.find_element_by_partial_link_text(partial_link_text).text
    driver.find_element_by_partial_link_text(partial_link_text).click()
    logger.info("点击'" + ele_text + "'")


def ele_click_by_accessibility_id(driver, accessibility_id):
    ele_text = driver.find_element_by_accessibility_id(accessibility_id).text
    driver.find_element_by_accessibility_id(accessibility_id).click()
    logger.info("点击'" + ele_text + "'")


def ele_click_by__android_uiautomator(driver, uia_string):
    ele_text = driver.find_element_by_android_uiautomator(uia_string).text
    driver.find_element_by_android_uiautomator(uia_string).click()
    logger.info("点击'" + ele_text + "'")


def ele_click_by_andriod_viewtag(driver, viewtag):
    ele_text = driver.find_element_by_android_viewtag(viewtag).text
    driver.find_element_by_android_viewtag(viewtag).click()
    logger.info("点击'" + ele_text + "'")


def ele_click_by_custom(driver, selector):
    ele_text = driver.find_element_by_custom(selector).text
    driver.find_element_by_custom(selector).click()
    logger.info("点击'" + ele_text + "'")


def ele_click_by_tag_name(driver, tag_name):
    ele_text = driver.find_elements_by_tag_name(tag_name).text
    driver.find_elements_by_tag_name(tag_name).click()
    logger.info("点击'" + ele_text + "'")


def alert_text_get(driver):
    logger.info("Alert text='" + driver.switch_to_alert().text + "'")
    return driver.switch_to_alert().text


def alert_accept(driver):
    logger.info("Accept alert")
    driver.switch_to_alert().accept()


def alert_dismiss(driver):
    logger.info("Dismiss alert")
    driver.switch_to_alert().dismiss()


def ele_send_keys(ele, text):
    logger.info("文本框传值'" + text + "'")
    ele.send_keys(text)


def ele_clear(ele):
    logger.info("清空文本框")
    ele.clear()


def swipe_left(driver, swipe_times=1):
    logger.info("向左滑动" + str(swipe_times) + "次")
    size = driver.get_window_size()
    width = size["width"]
    height = size["height"]
    for i in range(0,swipe_times):
        driver.swipe(width*0.8,height*0.5, width*0.2,height*0.5, duration=800)
        # time.sleep(1)


def swipe_right(driver, swipe_times=1):
    logger.info("向右滑动" + str(swipe_times) + "次")
    size = driver.get_window_size()
    width = size["width"]
    height = size["height"]
    for i in range(0,swipe_times):
        driver.swipe(width*0.2,height*0.5,width*0.8,height*0.5)
        time.sleep(1)


def swipe_up(driver, swipe_times=1):
    logger.info("向上滑动" + str(swipe_times) + "次")
    size = driver.get_window_size()
    width = size["width"]
    height = size["height"]
    for i in range(0,swipe_times):
        driver.swipe(width*0.5,height*0.8,width*0.5,height*0.2)
        time.sleep(1)


def swipe_down(driver, swipe_times=1):
    logger.info("向下滑动" + str(swipe_times) + "次")
    size = driver.get_window_size()
    width = size["width"]
    height = size["height"]
    for i in range(0,swipe_times):
        driver.swipe(width*0.5,height*0.2,width*0.5,height*0.8)
        time.sleep(1)
