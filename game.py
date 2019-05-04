# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:49:21 2019

@author: Oshi
"""

from dotsandboxes import dotsBoxesEnv
from dotsandboxes import reward
from agent import qAgent
#from qLearning import qLearn

class game:
    def __init__(self, 
                 _env: dotsBoxesEnv, 
                 _agent1:qAgent, 
                 _agent2:qAgent):
        self.env = _env
        self.agent1 = _agent1
        self.agent2 = _agent2
        self.reward = reward()
        # Q Class that will get updated by both agents
    
    def resetGame(self):
        # only reset environment
        self.env.reset()
    
    def playGameAndLearn(self,qClassInput):
        agent1action = []
        prevState1 = self.env.currState
        agent1action = 0
        totalAgent1Boxes = 0
        agent2action = []
        prevState2 = self.env.currState
        agent2action = 0
        totalAgent2Boxes = 0
        winner = 0 # draw0
        turn = 0
        # agents take turns
        while not self.env.done:
            myTurn = 1
            while myTurn>0 and not self.env.done:
                R1 =0
                prevState1 = self.env.currState
                agent1action = self.agent1.getAction(qClassInput,
                                                     self.env.currState,
                                                     self.env.possibleActions())
                boxesCompleted1 = self.env.doAction(agent1action)
                R1 = self.reward.reward4box(boxesCompleted1)
                totalAgent1Boxes += boxesCompleted1
                myTurn = boxesCompleted1
                # learn
                qClassInput.updateTable(prevState1,
                          agent1action,
                          self.env.currState,
                          R1)
                turn+=1
            

            if self.env.done:
                break
            
            myTurn_ = 1
            while myTurn_>0 and not self.env.done:
                R2 = 0
                # store previous state
                prevState2 = self.env.currState
                # get agent action from policy
                agent2action = self.agent2.getAction(qClassInput,
                                                     self.env.currState,
                                                     self.env.possibleActions())
                # do action and calculate reward
                boxesCompleted2 = self.env.doAction(agent2action)
                R2 = self.reward.reward4box(boxesCompleted2)
                totalAgent2Boxes += boxesCompleted2
                myTurn_ = boxesCompleted2
                # learn
                qClassInput.updateTable(prevState2,
                                  agent2action,
                                  self.env.currState,
                                  R2)
                turn+=1
            
        # learn from the win
        if totalAgent1Boxes == totalAgent2Boxes:
            winner = 0
        elif totalAgent1Boxes>totalAgent2Boxes:
            winner = 1
        else: 
            winner = 2
 
        
        if winner == 1:
            R1 = self.reward.reward4win()
            # learn
            qClassInput.updateTable(prevState1,
                              agent1action,
                              self.env.currState,
                              R1)
            self.agent1.wins += 1
            print("Winner Agent 1: ", totalAgent1Boxes)
        elif winner == 2:
            qClassInput.updateTable(prevState2,
                          agent2action,
                          self.env.currState,
                          R2)
            self.agent2.wins += 1
            print("Winner Agent 2: ", totalAgent2Boxes)
        else:
            self.agent1.draws += 1
            self.agent2.draws += 1
            print("Draw")
            
        return qClassInput
            