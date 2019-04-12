#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/3/18 15:14
#@Author: liuweilong
#@File  : desired_caps.py
from appium import webdriver
import yaml
import logging
import logging.config

con_log = '../log/log.conf'
logging.config.fileConfig(con_log)
logging = logging.getLogger()

def appium_desired():
    file = open('../yaml/family.yaml','r')
    data = yaml.load(file)
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platforVersion'] = data['platforVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['app'] = data['app']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    logging.info('start app...')
    dirver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    dirver.implicitly_wait(8)
    return dirver



if __name__ == '__main__':
    appium_desired()

#这是封装app启动的方法












