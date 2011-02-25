'''
Contains sample classes and situations that we want to test.
'''

# Can test module import
from collections import deque

class SampleBase(object):

  a_class_value = 'sample in a jar'

  # Can test __init__
  # Can test variable args
  # Can test changing module import
  def __init__(self, *args, **kwargs):
    self._args = args
    self._kwargs = kwargs
    self._prop_value = 5
    self._deque = deque()

  # Can test a simple property getter
  @property
  def prop(self):
    return self._prop_value

  # Can test property setter
  @prop.setter
  def set_property(self, val):
    self._prop_value = val

  # Can test property deleter
  @prop.deleter
  def del_property(self):
    self._prop_value = None

  # Can test a class method
  @classmethod
  def a_classmethod(cls):
    return cls.a_class_value

  # Can test a bound method
  def bound_method(self, arg1, arg2='two'):
    self._arg1 = arg1
    self._arg2 = arg2

  # Can test that we call another method
  def callback_source(self):
    self.callback_target()
  def callback_target(self):
    self._cb_target = 'called'


class SampleChild(SampleBase):

  # Can test calling super
  # Can test when bound method is overloaded
  def bound_method(self, arg1, arg2='two', arg3='three'):
    super(SampleBase,self).bound_method(arg1, arg2)
    self._arg3 = arg3

  # Can test overloading classmethod
  @classmethod
  def a_classmethod(cls):
    return 'fixed value'

  # Can test overloading a property
  @property
  def prop(self):
    return 'child property'
