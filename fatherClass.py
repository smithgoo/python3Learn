#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print 'Animal is running....'
        pass

class Dog (Animal):

    def run(self):
        print 'Dog is Running ....'
        pass
    pass

class cat (Animal):
    pass

dog = Dog();

dog.run()

flg = isinstance(dog,Dog)


print '%s',flg


def run_twice(animal):
    animal.run()
    animal.run()
    pass

run_twice(Animal())

print type(123)

print type('str')

print type(None)

let = type(123) ==type('str')

print let

print dir('ABC')

print len('ABC')

print 'ABC'.lower()



class MyObject(object):
    """docstring for MyObject."""
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x
        pass

obj = MyObject()

print obj

print hasattr(obj,'x')

print obj.x


print setattr(obj,'y',9)

print hasattr(obj,'y')

# print getattr(obj,'z');
