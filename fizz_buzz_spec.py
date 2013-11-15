#!/usr/bin/env python
# -*- coding: utf8 -*-

import unittest

from fizz_buzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
  def setUp(self):
    self.fizz_buzz = FizzBuzz()

  def test_fizz(self):
    self.assertEqual('Fizz', self.fizz_buzz.translate(3))
    self.assertEqual('Fizz', self.fizz_buzz.translate(6))
    self.assertEqual('Fizz', self.fizz_buzz.translate(9))

if __name__ == '__main__':
  unittest.main()
