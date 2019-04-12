#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/3/18 15:45
#@Author: liuweilong
#@File  : common_fun.py
from page_objectname.baseview import BaseView
from page_objectname.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By

class Common(BaseView):
    cancelBtn = (By.ID,'ID')
    skipBtn = (By.ID,'ID')

    def check_cancelBtn(self):
        logging.info('')
        try:
            cancelBtn = self.driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl')
        except NoSuchElementException:
            print('no')
        else:
            cancelBtn.click()


