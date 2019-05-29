#!/usr/bin/env python
# -*- coding: utf-8 -*-

fb = open("hello.text","w")

fb.write("hello world c++")

fp =open("hello.text","r")

buff =fp.read()

# help(fp)

fb.mode

fp.mode



print fb.closed
