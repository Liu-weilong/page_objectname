#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/3/18 15:56
#@Author: liuweilong
#@File  : loginview.py
import logging
from page_objectname.common_fun import Common
from page_objectname.desired_caps import appium_desired
from selenium.webdriver.common.by import By


class loginView(Common):
    username = (By.ID,'ID')
    password = (By.ID,'ID')
    loginbtn = (By.ID,'id')

    def login_action(self):
        self.check_cancelBtn()
        self.checkskin()

        logging.info('log....')
        self.dirver.find_element('')


if __name__ == '__main__':
    login_action()


