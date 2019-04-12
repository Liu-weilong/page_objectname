#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/3/18 15:42
#@Author: liuweilong
#@File  : baseview.py
class BaseView(object):
    def __init__(dirver):
        self.dirver=dirver

    def find_element(self,*loc):
        return self.dirver.find_element(*loc)