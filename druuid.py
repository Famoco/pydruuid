import time
import random

ALPHABET = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SHIFT = 64 - 41


class Druuid(object):
    def __init__(self, druuid=None):
        if druuid:
            self.druuid = druuid
        else:
            self._gen()

    def _gen(self):
        ms = int(round(time.time() * 1e3))
        rand = int(round(random.SystemRandom().random() * 1e16))
        self.druuid = ms << SHIFT | rand % (2 ** SHIFT)

    @property
    def time(self):
        return time.ctime((self.druuid >> SHIFT) / 1000)
