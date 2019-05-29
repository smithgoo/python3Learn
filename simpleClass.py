#!/usr/bin/env python
# -*- coding: utf-8 -*-

std1 ={'name':'michael','age':'18'}


def print_age(std):
    print '%s' % std['age']
    pass

print_age(std1)


class Student(object):

    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        pass
    def print_age1(self):
        print '%s' % self.__name
        pass

    def get_name(self):
        return self.__name
    pass

    def get_age(self):
        return self.__age
        pass

    def set_age(self,age):
        self.__age =age
        pass
    def set_name(self,name):
        self.__name =name
        pass

bat =Student('Bart Simpson',59)

# print bat
# print bat.name

def print_score(std):
    print '%s: %s'% (std.__name,std.__age)
    pass
# print_score(bat)
