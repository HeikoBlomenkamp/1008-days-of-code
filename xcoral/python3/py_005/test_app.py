#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 13:40:18 2022

@author: heiko
"""

from app import charAt, indexOf, returnX, numberAdd
from app import numberSub, numberDiv, numberMul


def test_first_charAt():
    assert charAt("Giraffe Academy", 0) == "G"

def test_fourth_charAt():
    assert charAt("Giraffe Academy", 3) == "a"

def test_first_indexOf():
    assert indexOf("Giraffe Academy", "G") == 0

def test_fourth_indexOf():
    assert indexOf("Giraffe Academy", "a") == 3

def test_returnX():
    assert returnX(-2.0987) == -2.0987

def test_numberAdd():
    assert numberAdd(10, 2.5) == 12.5

def test_numberSub():
    assert numberSub(10, 2.5) == 7.5

def test_numberDiv():
    assert numberDiv(10, 2.5) == 4.0

def test_numberMul():
    assert numberMul(10, 2.5) == 25.0
  