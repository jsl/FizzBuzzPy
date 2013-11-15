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

  def test_buzz(self):
    self.assertEqual('Buzz', self.fizz_buzz.translate(5))
    self.assertEqual('Buzz', self.fizz_buzz.translate(10))
    self.assertEqual('Buzz', self.fizz_buzz.translate(20))

  def test_fizz_buzz(self):
    self.assertEqual('FizzBuzz', self.fizz_buzz.translate(15))
    self.assertEqual('FizzBuzz', self.fizz_buzz.translate(30))
    self.assertEqual('FizzBuzz', self.fizz_buzz.translate(45))


  def test_sequence(self):
    expected_output = [1, 2, 'Fizz', 4, 'Buzz', 6, 7, 8, 'Fizz', 10, 11, 'Fizz', 13, 14, 'FizzBuzz']
    input_seq = range(1, 16)

    self.assertEqual(expected_output, self.fizz_buzz.translate(input_seq))

if __name__ == '__main__':
  unittest.main()
