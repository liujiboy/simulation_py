from model import City
from model import Human
from model import Simulation
import matplotlib.pyplot as plt
import matplotlib.animation as ma
sim=Simulation(2000,0.1,0.2)
map=plt.imread("resources/map.png")
plt.imshow(map)
scInfected=plt.scatter([],[],10, color='r')
scUnInfected=plt.scatter([],[],10,color='g')
def update(number):
    sim.run()
    print("迭代次数：%d,感染人数：%d，健康人数：%d"%(sim.iteration,sim.infected,sim.uninfected))
    pos=sim.getHumanPosition()
    scInfected.set_offsets(pos["infected"])
    scUnInfected.set_offsets(pos["uninfected"])

anim = ma.FuncAnimation(plt.gcf(), update, interval=1)
plt.show()