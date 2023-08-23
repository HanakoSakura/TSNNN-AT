'''
[WARNING:Attention to mental disorder]
'''
SampleRate = 64000

import math
import matplotlib.pyplot as plt
import random
import output

def SinWave(x:float):
    return math.sin(2*math.pi*x)

def draw(w:list[float]):
    plt.plot(range(len(w)),w)
    plt.show()

def NoiseMaker(length:int)->list[float]:
    tmp = []
    for i in range(length):
        tmp.append(random.random()*1.6-0.8)
    return tmp


# First order RC low-pass filter
class FO_RC_LPF:
    def __init__(self,A:float) -> None:
        self.A = A
        self.L = 0.0
    def filter(self,N:float):
        self.L = self.A * N + (1.0 - self.A) * self.L
        return self.L
    


if __name__ == '__main__' :
    
    
    
    pass

