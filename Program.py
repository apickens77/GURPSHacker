import random
import time

class Program:
    __name = ""
    __skillLvl = 0
    __complexity = 0
    __chal = 0

    def __init__(self, name, skill):
        self.__name = name
        self.__skill = skill

    def skillCheck(self):
        name = "Running " + self.__name +".exe...\n"
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        r3 = random.randint(1, 6)
        rsum = r1 + r2 + r3


        roll = r1, r2, r3
        roll = str(roll)
        stmt = name + "Skill: " + str(self.__skillLvl) + "\nRoll: " + str(rsum) + roll + "\n"

        #returns one value to print contents of roll and one for its success
        return stmt, rsum <= self.__skillLvl + self.__chal


    def irlSkillCheck(self, roll):
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        r3 = random.randint(1, 6)
        rsum = r1 + r2 + r3

        roll = r1, r2, r3
        roll = str(roll)
        
        return rsum <= self.__skillLvl


    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getSkillLvl(self):
        return self.__skillLvl

    def setSkillLvl(self, skill):
        self.__skillLvl = skill

    def getComplexity(self):
        return self.__complexity

    def setComplexity(self, comp):
        self.__complexity = comp

    def getChallenge(self):
        return self.__chal

    def setChallenge(self, chal):
        self.__chal = chal


class Breach(Program):
    def __init__(self, skill):
        self.setName("Breach")
        self.setSkillLvl(skill)

    
class Analyze(Program):
    def __init__(self, skill):
        self.setName("Analyze")
        self.setSkillLvl(skill)
