'''
Core curses.
'''

from math import pi,sin,cos

def Synth(
    voice:function = lambda x:0.0, # 音色
    freq:float = 1.0, # 频率(音高)
    vol:float = 1.0, # 音量
    length:int = 0,
    envelop:function = lambda x : 1.0, # 包络
    glide:function = lambda x : 1.0, # 滑音
    SampleRate = 64000 # ! Don't change it most of the time.
)->list[float]:
    w = []
    for i in range(length):
        s = i/SampleRate
        r = vol * envelop(s) * voice( glide(s) * freq * s ) 
        w.append(r)
    return w

def addTrack(src:list[float],_add:list[float]):
    l1 = len(src)
    l2 = len(_add)
    if l2 > l1 :
        tmp = [0.0]*l2
        for i in range(l2):
            if i < l1:
                tmp[i] = src[i]
            tmp[i]+=_add[i]
    else :
        tmp = [0.0]*l1
        for i in range(l1):
            if i < l2:
                tmp[i] = _add[i]
            tmp[i] += src[i]
    return tmp

def Volume(w:list[float],vol:float):
    tmp = [0.0]*len(w)
    for i in range(len(w)):
        tmp[i] = w[i]*vol
    return tmp

def Envelop(w:list[float],env:function,SampleRate=64000):
    tmp = [0.0]*len(w)
    for i in range(len(w)):
        tmp[i] = w[i]*env(i/SampleRate)
    return tmp
    
def sinc(x:float):
    return sin(pi*x)/(pi*x)

