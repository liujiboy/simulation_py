import random
import numpy as np
class City():
    def __init__(self,fileName):
        super().__init__()
        with open(fileName,"r") as f:
            self.w=int(f.readline())
            self.h=int(f.readline())
            self.cell=int(f.readline())
            self.map=[ ['0' for col in range(0,self.w)] for row in range(0,self.h)]
            for row in range(0,self.h):
                line=f.readline()
                for col in range(0,self.w):
                    self.map[row][col]=line[col]
    def canMove(self,x,y):
        if x>=0 and x<self.w and y>=0 and y<self.h:
            return self.map[y][x]=='0';
        else:
            return False;
class Human():
    def __init__(self,x,y,city,infected=False):
        super().__init__()
        self.x=x
        self.y=y
        self.city=city
        self.infected=infected
    def move(self):
        r=random.randint(0,3)
        if r==0:
            if self.city.canMove(self.x+1,self.y):
                self.x+=1
        elif r==1:
            if self.city.canMove(self.x-1,self.y):
                self.x-=1
        elif r==2:
            if self.city.canMove(self.x,self.y+1):
                self.y+=1
        else:
            if self.city.canMove(self.x,self.y-1):
                self.y-=1
class Simulation:
    def __init__(self,humanSize,iRatio,p):
        super().__init__()
        self.city=City("resources/map.txt")
        self.p=p
        self.humans=[]
        for i in range(0,humanSize):
            while True:
                x=random.randint(0,self.city.w-1)
                y=random.randint(0,self.city.h-1)
                if self.city.map[y][x]=='0':
                    break
            self.humans.append(Human(x,y,self.city))
        for i in range(0,int(humanSize*iRatio)):
            self.humans[i].infected=True
        self.infected=int(humanSize*iRatio)
        self.uninfected=humanSize-self.infected
        self.iteration=0
    def run(self):
        self.iteration+=1
        for human in self.humans:
            human.move()
        for human in self.humans:
            for other in self.humans:
                if human!=other and human.x==other.x and human.y==other.y:
                    if human.infected and (not other.infected):
                        if random.random()<self.p:
                            other.infected=True
        self.infected=0
        for human in self.humans:
            if human.infected:
                self.infected+=1
        self.uninfected=len(self.humans)-self.infected
    def getHumanPosition(self):
        infectedPos=[]
        unInfectedPos=[]
        for i in range(len(self.humans)):
            if self.humans[i].infected:
                infectedPos.append((self.humans[i].x*self.city.cell+self.city.cell//2,self.humans[i].y*self.city.cell+self.city.cell//2))
            else:
                unInfectedPos.append((self.humans[i].x*self.city.cell+self.city.cell//2,self.humans[i].y*self.city.cell+self.city.cell//2))
        return {"infected":np.array(infectedPos),"uninfected":np.array(unInfectedPos)}

# sim=Simulation(500,0.1,0.1)
# for i in range(100):
#     sim.run()
#     print("迭代次数：%d,感染人数：%d，健康人数：%d"%(sim.iteration,sim.infected,sim.uninfected))

