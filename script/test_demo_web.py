# -*- coding: utf-8 -*-
# @Time    : 2020-05-23
# @Author  : 爱吃苹果的鱼

from framework.base import selenium_init
from framework.base import selenium_action
import allure
import time
import pytest


@allure.feature('feature_web_demo')
class TestDemo:

    @pytest.fixture(scope='function')
    def setup(self):
        self.webInit = selenium_init.SeleniumInit()
        self.driver = self.webInit.setup('web')
        self.webAct = selenium_action.SeleniumActionAPI(self.driver)

    @pytest.mark.web
    @allure.story('test_story_of_web_demo')
    def test_web_demo(self, setup):
        self.webAct.to_url("http://www.baidu.com")
        self.webAct.ele_send_keys(self.webAct.ele_get_by_id('kw'), 'selenium') # 传入搜索关键字
        self.webAct.ele_click_by_id('su')  # 点击百度一下按钮
        time.sleep(3)
        result_list = self.webAct.ele_list_get_by_xpath("//div[@class='result c-container ']/h3/a")
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
