#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 13:40:18 2022

@author: heiko
"""

from app import numberAbs, numberPow, numberMax
from app import numberMin, numberRound


def test_numberAbs():
    assert numberAbs(-2.0987) == 2.0987

def test_numberPow():
    assert numberPow(4, 6) == 4096

def test_numberMax():
    assert numberMax(4, 6) == 6

def test_numberMin():
    assert numberMin(4, 6) == 4

def test_down_numberRound():
    assert numberRound(3.2) == 3

def test_up_numberRound():
    assert numberRound(3.7) == 4
