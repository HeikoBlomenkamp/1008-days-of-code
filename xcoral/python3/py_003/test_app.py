#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 13:40:18 2022

@author: heiko
"""


from app import hello

def test_classic_hello():
    
    # return should be the classic string
    assert hello() == "hello, world"


def test_modern_hello():
    
    # return should NOT be the modern string
    assert hello() != "Hello World!"
