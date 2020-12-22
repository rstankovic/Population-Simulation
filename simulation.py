import random
import seaborn as sns
import matplotlib.pyplot as plt


startingPopulation = 50
infantMortality = 25
agriculture = 5 #amount of food each year that one pop produces
disasterChance = 10
food = 0 #stockpile of food
fertilityx = 18 #earlist a woman can be fertile
fertilityy = 35 #latest a woman can be fertile

peopleDictionary = []

class Person:
    def __init__(self, age):
        self.gender = random.randint(0,1)
        self.age = age #first 50 will not all be 0 years old
        
'''
1. All 'able' people over 8 years old work to produce food
2. certain # of women in fertility band give birth every year
3. anyone over 80 dies
'''

def harvest(food, agriculture):
    ablePeople = 0
    for person in peopleDictionary:
        if person.age >8:
            ablePeople +=1
            
    food += ablePeople * agriculture
    
    if food < len(peopleDictionary): #food is stockpile, remember
        del peopleDictionary[0:int(len(peopleDictionary) - food)]
        food = 0
    else: food -= len(peopleDictionary)
#here, since one unit of food sustains one person, any person without food dies

def reproduce(fertilityx, fertilityy):
    for person in peopleDictionary:
        if person.gender == 1:
            if person.age > fertilityx:
                if person.age < fertilityy:
                    if random.randint(0,5)==1:
                        if random.randint(0,100)>infantMortality:
                            peopleDictionary.append(Person(0))

#here it is assumed that 1 in 5 women will become pregnant every year. if any person is female b/n 18 and 35, they have 20% chance to give birth, adding new person of age 0 to population

#could be generally done with math but laying out code as object-based script allows for more flexibility, visualization

def beginSim():
    for x in range(startingPopulation):
        peopleDictionary.append(Person(random.randint(18,50)))


def runYear(food, agriculture, fertilityx, fertilityy, infantMortality, disasterChance, popList):
    harvest(food, agriculture)
    reproduce(fertilityx, fertilityy)
    for person in peopleDictionary:
        if person.age > 80:
            if random.randint(0,2) ==1: #not always gonna die at 80
                peopleDictionary.remove(person)
        else:
            if random.randint(0,10000) != 500: #arbitrary number, but also random chance of death throughout lifetime
                person.age +=1
            else:
                peopleDictionary.remove(person)
    
    print('Current Population: ', len(peopleDictionary))
    popList.append(len(peopleDictionary))
    
    if random.randint(0,100) < disasterChance:
        del peopleDictionary[0:int(random.uniform(0.05, 0.2)*len(peopleDictionary))]
    print(len(peopleDictionary))
    infantMortality *= 0.985
    return infantMortality
    
popList = []
beginSim()
while len(peopleDictionary)<100000 and len(peopleDictionary) > 1:
    infantMortality = runYear(food, agriculture, fertilityx, fertilityy, infantMortality, disasterChance, popList)

plt.plot(popList)
plt.show()
