# encoding: utf-8
# Created by Jeremy Bowman on Thu Feb 20 16:55:15 EST 2014
# Copyright (c) 2014 Safari Books Online. All rights reserved.
"""
Yet Another Django Profiler middleware

A django profiling middeware that tries to consolidate the best features of
the ones that came before it.  Originally described at
http://blog.safariflow.com/2013/11/21/profiling-django-via-middleware/
"""
from .profiler_middleware import ProfilerMiddleware

__version__ = (0, 1, 0)