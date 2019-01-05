#coding:utf-8




import logging
import time


class mylogger(object):

    def __init__(self, name='mylogger'):
        if name != None:
            self.logger_s = logging.getLogger(name)
        elif not getattr(self, 'name', None):
            raise ValueError("%s must have a name" % type(self).__name__)

        self.logger.propagate = False
        self.logger.setLevel(level=logging.INFO)

        riqi = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        log_name = riqi + '.log'

        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger_s.addHandler(fh)
        self.logger_s.addHandler(ch)

    @property
    def logger(self):
        return self.logger_s



