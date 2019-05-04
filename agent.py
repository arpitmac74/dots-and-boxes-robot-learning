# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:42:16 2019

@author: Oshi
"""

from qLearning import qLearn

class qAgent:
    def __init__(self):
        self.wins = 0
        self.draws = 0
    
    def getAction(self, 
                  qClass : qLearn,
                  currStateIndex,
                  possibleActions):
        return qClass.eGreedyPolicy(currStateIndex,possibleActions)