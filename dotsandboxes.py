# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 18:16:55 2019

@author: Oshi
"""

import numpy as np
import itertools

class dotsandboxesenv:
    def __init__(self,
                 _size=2):
        self.size=_size
        self.numactions=((self.size+1)*(self.size))*2
        self.numstates= 2**(self.numactions)
        self.allStates=list(range())
        