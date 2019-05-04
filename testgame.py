# -*- coding: utf-8 -*-
"""
Created on Sat May  4 01:34:15 2019

@author: Oshi
"""

from dotsandboxes import dotsBoxesEnv
from agent import qAgent
from qLearning import qLearn
from game import game
from randomagent import rAgent

env = dotsBoxesEnv(2)
agent1 = qAgent()
agent2 = rAgent()
qClass = qLearn(env.numStates, env.numActions)
game1 = game(env, agent1, agent2)
#%%
qClass = game1.playGameAndLearn(qClass)
game1.resetGame()
