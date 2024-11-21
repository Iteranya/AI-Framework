# This is the Module
# Basically,  if you're looking to expand the SDK's current functionality...
# Just add new method here
# Adding new class unfortunately still doesn't work, (Yet), I'm working on it
# Feel free to customize it to your system~
from core.model import Character
import re

class ArtificialIntelligenceModule():
    def __init__(self):
        self.aiDict = []

    def stage(self,name:str):# Should I add GBNF here????
        result = {
            "type":"stage",
            "stage":name
        }
        self.aiDict.append(result)
        return result

    def instruction(self,persona:str,instruction:str,example:list): # Or here???
        result = {
            "type":"instruction",
            "persona":persona,
            "instruction":instruction,
            "example":example
        }
        self.aiDict.append(result)
        return result
    
    def context(self,context:str):
        result = {
            "type":"context",
            "context":context
        }
        self.aiDict.append(result)
        return result
    
    def reasoning(self,reasoning:map): # Turns into a GBNF
        result = {
            "type":"reasoning",
            "reasoning":reasoning
        }
        self.aiDict.append(result)
        return result
