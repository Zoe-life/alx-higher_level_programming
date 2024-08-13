#!/usr/bin/python3
class LockedClass:
  def __setattr__(self, __name__, __value__):
    if __name__ != 'first_name':
      raise AttributeError("'LockedClass' object has no attribute '{}'".format(__name__))
    self.__dict__[__name__] = __value__