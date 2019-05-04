# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:51:08 2019

@author: Oshi
"""

from dotsandboxes import dotsBoxesEnv
from agent import qAgent
from qLearning import qLearn
from game import game
from randomagent import rAgent

games2Play = 100
def train(games2Play,
          _game:qAgent,
          _qClass):
    numGame = 0
    while numGame < games2Play:
        _qClass = _game.playGameAndLearn(_qClass)
        _game.resetGame()
        numGame+=1
    return _game.agent1.wins, _game.agent2.wins, _game.agent1.draws, _qClass
    
env = dotsBoxesEnv(2)# cahnge the number to 2 for 2x2 training or 3 for 3x3 training
agent1 = qAgent() 
agent2 = qAgent()#change to random agent for random game training(rAgent)
qClass = qLearn(env.numStates, env.numActions)
game1 = game(env, agent1, agent2)

agent1Wins, agent2Wins, draws, qClass = train(games2Play,game1,qClass)
print(agent1Wins, agent2Wins, draws)