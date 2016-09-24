# -*- coding: UTF-8 -*-
import sys

print "你好" == u"你好"
# False

reload(sys)
sys.setdefaultencoding("utf-8")

print "你好" == u"你好"
# True
