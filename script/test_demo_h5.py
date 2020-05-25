# -*- coding: utf-8 -*-
# @Time    : 2020-05-23
# @Author  : 爱吃苹果的鱼

import time
from framework.base import selenium_init
from framework.base import selenium_action
import allure
import pytest


@allure.feature('feature_h5_demo')
class TestH5Demo:

    @pytest.fixture(scope='function')
    def setup(self):
        self.h5Init = selenium_init.SeleniumInit()
        self.driver = self.h5Init.setup('h5')
        self.webAct = selenium_action.SeleniumActionAPI(self.driver)

    @pytest.mark.h5
    @allure.story('test_story_of_h5_demo')
    def test_h5_demo(self, setup):
        self.webAct.to_url("http://www.baidu.com")
        self.webAct.ele_send_keys(self.webAct.ele_get_by_id('index-kw'), 'selenium')  # 传入搜索关键字
        self.webAct.ele_press_enter(self.webAct.ele_get_by_id('index-kw'))
        time.sleep(3)
        result_list = self.webAct.ele_list_get_by_xpath("//div[@class='c-result-content']//span[@class='c-title-text']")
        result = False
        for i in range(len(result_list)):
            if 'selenium' in str(result_list[i].text).lower():
                result = True
            else:
                print(result_list[i].text + '：不包含selenium')
                result = False
        assert result

    def teardown(self):
        self.driver.quit()
