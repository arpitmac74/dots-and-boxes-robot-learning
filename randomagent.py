# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:57:01 2019

@author: Oshi
"""

from qLearning import qLearn

class rAgent:
    def __init__(self):
        self.wins = 0
        self.draws = 0
    
    def getAction(self, 
                  qClass : qLearn,
                  currStateIndex,
                  possibleActions):
        return qClass.randomPolicy(currStateIndex,possibleActions)