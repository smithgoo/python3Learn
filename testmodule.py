#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'kpeng'

import sys
try:
    import cStringIO as StringIO
    pass
except importError:
    import StringIO
    raise

def test():
    args =sys.argv
    if len(args) ==1:
        print 'Hello,World'
        pass
    elif len(args) ==2:
        print 'Hello,%s!' % args[1]

    else :
        print 'Too Many arguments!'
    pass

if __name__=='__main__':
    test()
    pass
