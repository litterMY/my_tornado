import os
import sys

if __name__ == "__main__":
    if sys.path[0]==os.path.dirname(__file__):
        del sys.path[0]

import functools
import logging
import os
import pkgutil
import sys
import traceback
import types
import subprocess
import weakref

from tornado import ioloop
from tornado.log import gen_log
from tornado import process
from tornado.util import exec_in

try:
    import signal

except ImportError:
    signal = None


_has_execv = sys.platform != 'win32'
_reload_hooks = []
_reload_attempted = False
_io_loops = weakref.WeakKeyDictionary()
_autoreload_is_main = False
_original_argv = None
_original_spec = None

def start(check_time=500):
    """
    开始观察源文件的变动
    """
    io_loop = ioloop.IOLoop.current()
    if io_loop in _io_loops:
        return
    _io_loops[io_loop] = True
    if(len(_io_loops))>1:
        gen_log.warning("tornado.autoreload started more than once in the same process")
    modify_times={}
    callback = functools.partial(_reload_on_update, modify_times)
    scheduler = ioloop.PeriodicCallback(callback, check_time)
    scheduler.start()


def _reload_on_update():
    pass