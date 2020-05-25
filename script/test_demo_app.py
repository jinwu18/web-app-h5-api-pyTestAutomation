# -*- coding: utf-8 -*-
# @Time    : 2020-05-23
# @Author  : 爱吃苹果的鱼

import pytest
import allure
from framework.base import appium_init
from framework.app.appcommon import AppCommon
from framework.base.selenium_action import SeleniumActionAPI
from framework.utils.string_utils import StringUtils
import time


@allure.feature('feature_app_demo')
class TestAppDemo:

    @pytest.fixture(scope='function')
    def setup(self):
        self.appInit = appium_init.AppiumInit('7.1.1', 'android', '192.168.174.101:5555', 'com.android.contacts',
                                        'com.android.contacts.activities.PeopleActivity', '4723')
        self.driver = self.appInit.setup()
        self.app = AppCommon(self.driver)
        self.appium = SeleniumActionAPI(self.driver)
        self.util = StringUtils()

    @pytest.mark.app
    @allure.story('test_story_of_app_demo')
    def test_app_demo(self, setup):
        self.app.tap_click(int(959*self.app.device_x_get()/1080), int(1670*self.app.device_y_get()/1794))
        # time.sleep(5)
        # self.appium.ele_click_by_id('com.android.contacts:id/left_button')
        time.sleep(2)
        edit_boxes = self.appium.ele_list_get_by_class_name("android.widget.EditText")
        self.appium.ele_send_keys(edit_boxes[0], self.util.name_get())
        self.appium.ele_send_keys(edit_boxes[1], self.util.phone_get())
        self.appium.ele_click_by_id('menu_save')
        result = self.app.toast_chk('联系人已保存')
        assert result

    def teardown(self):
        self.driver.quit()

